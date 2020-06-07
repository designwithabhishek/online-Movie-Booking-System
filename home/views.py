from django.shortcuts import render
from booking.models import Movies
import http.client
import json
# Create your views here.

def home_list(request):
    movies=Movies.objects.all()
    '''
    details = []
    for movie in movies:
        conn = http.client.HTTPSConnection("api.themoviedb.org")
        name=movie.name
        name=name.replace(' ','%20')
        payload = "{}"
        conn.request("GET",
                     "/3/search/movie?region=IN&primary_release_year=2019&include_adult=false&page=1&query="+name+"&language=en-US&api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c",
                     payload)
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data.decode("utf-8"))
        result['results'][0]['background']=movie.cover_page
        a = result['results'][0]
        newtitle=a['title']
        Movies.objects.filter(id=movie.id).update(name=newtitle)
        if a!=None:
            details.append(a)


    ...
    '''
    context={
             'movie_details':movies
            }

    return render(request,'home\index.html',context)