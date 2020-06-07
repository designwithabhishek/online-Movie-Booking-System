from django.urls import path
from . import views
from  django.conf.urls.static import static
from django.conf import settings
app_name="home"

urlpatterns=[
    path('',views.home_list,name="home_list")
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)