from django.urls import path
from .views import CommentsListCreateView, CommentsDetailView,AllCommentssListView,CommentsDeleteView,CommentsUpdateView,AllComments

urlpatterns = [
    path('/', CommentsListCreateView.as_view(), name='Comments-list-create'),
    path('/<int:pk>/', CommentsDetailView.as_view(), name='Comments-detail'),
    path('/all/', AllCommentssListView.as_view(), name='all-Commentss-list'),  
    path('/delete/<int:pk>/', CommentsDeleteView.as_view(), name='Comments-delete'), 
    path('/update/<int:pk>/', CommentsUpdateView.as_view(), name='Comments-update'), 
    path('/com/', AllComments.as_view(), name='all-comments'),
]