from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('myapp.urls')),  # Include the app's urls
    path('api/pred/', include('prediction.urls')),
    path('api/img/', include('image_processing.urls')),
    path('api/search/', include('imagesearch.urls')),  # Include the imagesearch app's URLs
    path('api/sent/', include('sentiment.urls')),
    path('api/store/', include('store.urls')),  # Add this line for the store app
    path('api/comments', include('comments.urls')),
    path('api/recom/', include('recommendation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
