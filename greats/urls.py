from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/<int:pk>', views.ArtistDetails.as_view(), name="artist_details"),
]