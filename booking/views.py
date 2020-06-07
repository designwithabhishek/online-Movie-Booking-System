from django.shortcuts import render,render_to_response
from django.template.loader import render_to_string
from django.core import serializers
from datetime import datetime
from .models import Show,Auditorium,Layouts,Movies
from django.http import JsonResponse,HttpResponse
import http.client
import json
import datetime
from django.utils import timezone
# Create your views here.


def booking_list(request,movieid):
    '''
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    name = name.replace(' ', '%20')
    payload = "{}"
    conn.request("GET",
                 "/3/search/movie?region=IN&primary_release_year=2019&include_adult=false&page=1&query=" + name + "&language=en-US&api_key=f9ce6f7c59d649e68f1d43b0ebb12e8c",
                 payload)
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data.decode("utf-8"))
    a = result['results'][0]
    '''
    all_shows=Show.objects.all()
    for show in all_shows:
        if show.date < datetime.date.today():
            show.delete()
        elif show.date == datetime.date.today():
            if show.start_time <= timezone.now().time():
                show.delete()
    available_shows=Show.objects.filter(movies__id=movieid)
    movies=Movies.objects.get(id=movieid)
    showtypes=Auditorium.objects.filter(show__movies__id=movieid).values().distinct()
    dates=list()

    #date_data['date']=datetime.datetime.today().strftime("%x")
    #date_data['day']=datetime.datetime.today().strftime("%a")
    #dates.append(date_data)
    for i in range(7):
        x=datetime.datetime.today()+datetime.timedelta(days=i)
        s=str(x.year)+"-"+str(x.month)+"-"+str(x.day)
        date_data = dict()
        date_data['date'] =s
        date_data['day'] =x.strftime("%a")
        dates.append(date_data)
   # audi_A=Audi_A.objects.all()
    #rows_name=Audi_A.objects.all().values('row').distinct()
    context={
        'movie_details':movies,
       # 'audiA':audi_A,
        #'audiA_rows':rows_name,
        'show_types':showtypes,
        'dates':dates
    }
    return render(request,"booking/book_tickets.html",context)

def filtering(request):
    if request.GET.get('movie'):
        selectedmovie=request.GET.get('movie')
        mname=Movies.objects.get(id=selectedmovie)
        request.session['movie']=selectedmovie
        request.session['movie_name']=mname.name
    #format=request.GET.get('format')
    if request.GET.get('format'):
        format=request.GET.get('format')
        available_shows = Show.objects.filter(movies__id=selectedmovie).filter(auditorium__audi_type=format).values()
        seatcount = Auditorium.objects.filter(audi_type=format).values('seat_count')
        audiname=Auditorium.objects.get(audi_type=format)
        request.session['audi_name']=audiname.audi_name
        request.session['format']=format
        #return JsonResponse({'shows': list(available_shows), 'seats': list(seatcount)})
    if request.GET.get('layout'):
        layout=request.GET.get('layout')
        active_layout=Layouts.objects.filter(layout_no=layout).values()
        price=Show.objects.filter(layout=layout).values('price')
        request.session['layout']=layout
        rows=Layouts.objects.filter(layout_no=layout).values('row').distinct()
                #price=Show.objects.filter(layout=layout).values('price')
        #request.session['price']=price[0]['price']
        return JsonResponse({'seats':list(active_layout),'available_rows':list(rows)})
    if request.GET.get('selected_date'):
        selected_date=request.GET.get('selected_date')
        selectedmovie=int(request.session['movie'])
        format =request.session['format']
        available_shows = Show.objects.filter(movies__id=selectedmovie).filter(auditorium__audi_type=format).filter(date=selected_date).values()
        seatcount = Auditorium.objects.filter(audi_type=format).values('seat_count')
        return JsonResponse({'shows': list(available_shows), 'seats': list(seatcount)})
    if(request.GET.get('seats')):
        request.session['seats']=request.GET.get('seats')
        message="Thanks for selecting seats"
        return HttpResponse(message)
    else:
        seatno=[]
        a=list(request.session['seats'].split(','))
        layout=request.session['layout']
        data=dict()
        data['movie']=request.session['movie_name']
        data['seats']=request.session['seats']
        data['format']=request.session['format']
        data['numberoftickets'] = len(a)
        data['price']=int((Show.objects.get(layout=layout)).price*len(a))
        data['audi']=request.session['audi_name']
        data['layout']=request.session['layout']
        return JsonResponse({'summary':(data)})