from  django.urls import path
from .views import booking_list,filtering
app_name="booking"

urlpatterns=[
    path('<int:movieid>',booking_list,name="booking_list"),
    path('filtering/',filtering,name="filter"),

]