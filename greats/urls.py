from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/<int:pk>', views.ArtistDetails.as_view(), name="artist_details"),
    path('reviews/', views.ReviewList.as_view(), name="review_list"),
    path('reviews/<int:pk>', views.ReviewDetails.as_view(), name="review_details"),
]