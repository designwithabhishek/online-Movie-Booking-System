from  django.urls import path
from .views import movie_details

app_name="movies"
urlpatterns=[
    path('',movie_details,name="movie_details")
]