import os
import shutil
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ultralytics import YOLO
from PIL import Image, ImageDraw
from django.conf import settings
import datetime
import uuid

# Define the class names for your model
CLASS_NAMES = {
    0: 'ladies_croptop',
    1: 'ladies_denim',
    2: 'ladies_denim_skirt',
    3: 'ladies_long_dress',
    4: 'ladies_long_skirt',
    5: 'ladies_longsleeve_blouse',
    6: 'ladies_longsleeve_tshirt',
    7: 'ladies_pants',
    8: 'ladies_short',
    9: 'ladies_short_dress',
    10: 'ladies_short_skirt',
    11: 'ladies_shortsleeve_blouse',
    12: 'ladies_sleeveless_blouse',
    13: 'men_denim',
    14: 'men_hoodies',
    15: 'men_longsleeve_shirt',
    16: 'men_longsleeve_tshirt',
    17: 'men_oversized_tshirt',
    18: 'men_pants',
    19: 'men_short',
    20: 'men_shortsleeve_shirt',
    21: 'men_tshirt'
}

# Load the YOLO model
def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'imagesearch', 'models', 'bestv1.pt')
    model = YOLO(model_path)
    return model

def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

class ObjectDetection(APIView):
    def post(self, request):
        print("Request received")
        model = load_model()
        print("Model loaded")

        uploaded_file = request.FILES.get('image')
        if not uploaded_file or not isinstance(uploaded_file, InMemoryUploadedFile):
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        file_name = os.path.basename(uploaded_file.name)
        file_name_without_ext = os.path.splitext(file_name)[0]
        file_extension = os.path.splitext(file_name)[1]

        image = Image.open(uploaded_file).convert('RGB')
        draw = ImageDraw.Draw(image)

        results = model.predict(source=image, conf=0.25)
        boxes = results[0].boxes.xyxy.cpu().numpy().tolist()
        confidences = results[0].boxes.conf.cpu().numpy().tolist()
        class_labels = results[0].boxes.cls.cpu().numpy().tolist()

        save_dir = os.path.join(settings.MEDIA_ROOT, 'detected_images')
        os.makedirs(save_dir, exist_ok=True)
        clear_directory(save_dir)

        cropped_images_paths = []

        for i, box in enumerate(boxes):
            class_label = CLASS_NAMES.get(class_labels[i], "unknown")
            cropped_file_name = f"{class_label}.jpg"
            cropped_image = image.crop((box[0], box[1], box[2], box[3]))
            cropped_image.save(os.path.join(save_dir, cropped_file_name))
            relative_path = os.path.join(cropped_file_name)
            cropped_images_paths.append(request.build_absolute_uri(settings.MEDIA_URL + relative_path))

            draw.rectangle(box[:4], outline="red", width=2)

        # Save the annotated image after drawing the boxes
        annotated_file_name = f"detected_{file_name}"
        annotated_image_path = os.path.join(save_dir, annotated_file_name)
        image.save(annotated_image_path)

        # Use forward slashes in URLs
        annotated_image_url = request.build_absolute_uri(settings.MEDIA_URL + 'detected_images/' + annotated_file_name.replace("\\", "/"))

        cropped_images_urls = []
        for path in cropped_images_paths:
            # Convert file paths to URLs and use forward slashes
            url_path = 'detected_images/' + os.path.basename(path).replace("\\", "/")
            cropped_image_url = request.build_absolute_uri(settings.MEDIA_URL + url_path)
            cropped_images_urls.append(cropped_image_url)

        data = {
            'boxes': boxes,
            'confidences': confidences,
            'class_labels': [CLASS_NAMES.get(cl, "unknown") for cl in class_labels],
            'annotated_image_path': annotated_image_url,
            'cropped_images_paths': cropped_images_urls
        }

        return Response(data, status=status.HTTP_200_OK)