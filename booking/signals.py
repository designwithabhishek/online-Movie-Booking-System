from django.db.models.signals import post_save
from django.core.signals import request_started
from  django.dispatch import receiver
from .models import Audi_layout,Show,Layouts,Movies,Cast,Mapper
from datetime import date,datetime
import http
import json
@receiver(post_save,sender=Show)
def creating_layout(sender,instance,**kwargs):
    audi = Audi_layout.objects.filter(auditorium=instance.auditorium).values()
    for obj in audi:
        Layouts.objects.create(seat_number=obj['seat_number'], row=obj['row'], layout_no=instance, status=False)


@receiver(post_save,sender=Movies)
def adding_cast(sender,instance,**kwargs):
    if instance.IMDB_id:
        if not Mapper.objects.filter(movie=instance):
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            payload = "{}"
            conn.request("GET", "/3/movie/" + str(instance.IMDB_id) + "/credits?api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c", payload)
            res = conn.getresponse()
            data = res.read()
            cast = json.loads(data.decode("utf-8"))
            casting = cast['cast']
            mycast=[]
            for obj in casting:
                c1=Cast.objects.create(name=obj['name'], character=obj['character'], cast_image=obj['profile_path'])
                Mapper.objects.create(movie=instance,cast=c1)
