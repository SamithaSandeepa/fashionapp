from rest_framework import generics
from .models import Comments
from .serializers import CommentsSerializer
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


from rest_framework import status
from rest_framework.response import Response

class CommentsListCreateView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
    
class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
class AllCommentssListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
class CommentsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    partial = True
    
    
class CommentsDeleteView(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Comments"))



class AllComments(APIView):
    def get(self, request, format=None):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        
        # Group comments by product_id
        grouped_comments = defaultdict(list)
        for comment in serializer.data:
            grouped_comments[comment['product_id']].append(comment['comments'])
        
        # Prepare the response data
        response_data = []
        for product_id, comments in grouped_comments.items():
            response_data.append({
                "product_id": product_id,
                "comment": comments
            })
            
        return Response(response_data)
