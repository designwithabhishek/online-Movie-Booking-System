from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.db.models import Q
from datetime import time
from .validation import validate_date_show
from  django.core.exceptions import ValidationError
from datetime import datetime,timedelta
import http.client
import json

class Cast(models.Model):
    name=models.CharField(max_length=50)
    character=models.CharField(max_length=30)
    cast_image=models.TextField(null=True)
    def __str__(self):
       return self.name

class Mapper(models.Model):
    movie=models.ForeignKey('Movies',on_delete=models.CASCADE)
    cast=models.ForeignKey(Cast,on_delete=models.CASCADE)

class Movies(models.Model):
    name=models.CharField(max_length=50)
    cover_page=models.ImageField(upload_to='movies',null=True,default=False)
    overview=models.TextField(default="Not available")
    poster_path=models.TextField(default="Not available")
    IMDB_id=models.IntegerField(null=True,editable=False)
    #showing_in=models.ManyToManyField('Auditorium',through='Show')

    class Meta:
        verbose_name='Movie'
        verbose_name_plural='Movies'

    def clean(self):

        if self.overview=="Not available" or self.poster_path=="Not available":
            conn = http.client.HTTPSConnection("api.themoviedb.org")
            name = self.name
            name = name.replace(' ', '%20')
            payload = "{}"
            conn.request("GET",
                         "/3/search/movie?region=IN&primary_release_year=2019&include_adult=false&page=1&query=" + name + "&language=en-US&api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c",
                         payload)
            res = conn.getresponse()
            data = res.read()
            result = json.loads(data.decode("utf-8"))
            if not len(result['results'])==0:
                self.overview=result['results'][0]['overview']
                self.name = result['results'][0]['title']
                self.poster_path = result['results'][0]['poster_path']
                self.IMDB_id=result['results'][0]['id']
            else:
                raise ValidationError("Unable to fetch data please add manually")



    def __str__(self):
        return self.name

class Auditorium(models.Model):
    audi_name=models.CharField(max_length=40)
    seat_count=models.IntegerField()
    audi_type=models.CharField(max_length=10)
    #audi_layout=models.ForeignKey('Audi_layout',on_delete=models.CASCADE)


    class Meta:
        verbose_name='Auditorium'
        verbose_name_plural='Auditoriums'
    def __str__(self):
        return self.audi_name

class Layouts(models.Model):
    seat_number = models.IntegerField()
    row = models.CharField(max_length=1,)
    layout_no=models.ForeignKey('Show',on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    class Meta:
        verbose_name='Layout'
        verbose_name_plural='Layouts'


class Show(models.Model):
    movies=models.ForeignKey(Movies,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    date=models.DateField(validators=[validate_date_show],null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    layout=models.AutoField(primary_key=True)
    auditorium=models.ForeignKey(Auditorium,on_delete=models.CASCADE,default=1)
    duration=models.IntegerField(null=True)
    def clean(self):
        all_shows=Show.objects.filter(Q(auditorium=self.auditorium ))
        selected_movie_show=Show.objects.filter(Q(auditorium=self.auditorium ) & Q(movies=self.movies))
        hour = int(int(self.end_time.hour) * 60 - int(self.start_time.hour) * 60)
        current_time=datetime.now()
        current_day=datetime.now().date()
        required_time=(current_time + timedelta(hours=6)).time()
        self.duration = hour
        cyclic_required_time=time(18,0,0)
        r_time=datetime.now().time()
        #raise ValidationError(r_time)
        if self.start_time >= self.end_time:
            raise ValidationError("Start Time must be Less then Endtime")
        if self.start_time < required_time and self.date == current_day:
            raise ValidationError("Invalid Time Time must be atleast "+str(required_time))
        if r_time>=cyclic_required_time and self.date == current_day:
            raise ValidationError("Invalid date we have a cooldown period of 6 hrs since after 6 hrs next day will begin please correct your date field");
        for show in all_shows:
            if ((show.start_time <= self.start_time <=show.end_time ) or (show.start_time <= self.end_time <=show.end_time )) and self.date == show.date:
                raise ValidationError(str(show.auditorium)+" is already occupied by "+str(show.movies)+" from "+str(show.start_time)+" to "+str(show.end_time))
        for show in selected_movie_show:
            if self.duration!=show.duration:
                raise ValidationError("Incorrect End time show must be of "+str(show.duration))


    class Meta:
        verbose_name='Show'
        verbose_name_plural='Shows'



class Audi_layout(models.Model):
    auditorium=models.ForeignKey(Auditorium,on_delete=models.CASCADE)
    seat_number=models.IntegerField()
    row=models.CharField(max_length=1)
    class Meta:
        verbose_name='Audi_layout'
        verbose_name_plural='Audi_layouts'


class Reviews(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    movie_name=models.ForeignKey('Movies',on_delete=models.CASCADE)
    message=models.TextField()
    image=models.ImageField(upload_to="user",default='adult-boy-casual-220453.jpg')
    class Meta:
        verbose_name='Review'
        verbose_name_plural='Reviews'
