from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>', views.PostDetails.as_view(), name="post_details"),
]