from django.shortcuts import render
from booking.models import Movies,Reviews,Cast
from django.contrib import messages
import http.client
import json
# Create your views here.

def  movie_details(request,movieid):
    '''
    movieid=str(movieid)
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    payload = "{}"
    conn.request("GET", "/3/movie/"+movieid+"?language=en-US&api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c", payload)
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data.decode("utf-8"))
    #result[0]['background'] = movies.cover_page
    title=result['title']
    movies = Movies.objects.get(name__icontains=title)
    result['background'] = movies.cover_page
    conn.request("GET", "/3/movie/"+movieid+"/credits?api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c", payload)
    res = conn.getresponse()
    data = res.read()
    cast=json.loads(data.decode("utf-8"))
    casting=cast['cast']
    if result!= None:
        details=result
    '''
    #review form
    movies=Movies.objects.get(id=movieid)
    casting=Cast.objects.filter(mapper__movie=movieid)
    if request.method=='POST':
        name=request.POST.get('name')
        image=request.FILES.get('image')
        if not image:
            image="user/adult-boy-casual-220453.jpg";
        message=request.POST.get('message')
        rating=int(request.POST.get('starrating'))
        Reviews.objects.create(name=name,image=image,message=message,movie_name=movies,rating=rating)
        messages.success(request,"Thanks for your Feedback")
    reviews=Reviews.objects.filter(movie_name=movies)
    context = {
        'movie_details': movies,
        'casting':casting,
        'reviews':reviews
    }

    return render(request,'movies\movie-details.html',context)
