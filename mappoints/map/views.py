from django.shortcuts import render
from .models import Accident
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/account/login/')
def mappoints(request):
    p =  Accident.objects.all()
    #mpoints =  serializers.serialize("json", mpoints)
    mpoints=[]
    points=[]
    for i in p:
        a={}
        s={}
        a['ac']=i.ac
        a['year']=i.year
        a['month']=i.month
        a['day']=i.day
        a['date']=i.date
        a['hour']=i.hour
        a['minute']=i.minute
        a['address']=i.address
        a['roadtype']=i.roadtype
        a['text']=i.text
        a['dead']=i.dead
        a['hurt']=i.hurt
        a['weather']=i.weather if i.weather else ''
        a['rain']=i.rain if i.rain else ''
        a['wind']=i.wind if i.wind else ''
        a['temp']=i.temp if i.temp else ''
        a['naturl']=i.naturl if i.naturl else ''
        a['p1_name']=i.p1_name
        a['p1_birthday']=i.p1_birthday
        a['p1_age']=i.p1_age if i.p1_age else ''
        a['p1_id']=i.p1_id
        a['p1_driveyear']=i.p1_driveyear
        a['p1_type']=i.p1_type
        a['p1_dayget']=i.p1_dayget
        a['p1_cartype']=i.p1_cartype
        a['p1_numoncar']=i.p1_numoncar
        a['p1_carid']=i.p1_carid
        a['p1_blame']=i.p1_blame
        a['p1_sex']=i.p1_sex
        a['p2_name']=i.p2_name
        a['p2_birthday']=i.p2_birthday
        a['p2_age']=i.p2_age if i.p2_age else ''
        a['p2_id']=i.p2_id
        a['p2_driveyear']=i.p2_driveyear
        a['p2_type']=i.p2_type
        a['p2_dayget']=i.p2_dayget
        a['p2_cartype']=i.p2_cartype
        a['p2_numoncar']=i.p2_numoncar if i.p2_name else ''
        a['p2_carid']=i.p2_carid
        a['p2_blame']=i.p2_blame
        a['p2_sex']=i.p2_sex
        a['city']=i.city
        a['lng']=i.lng
        a['lat']=i.lat
        a['time']=str(i.hour)+':'+str(i.minute) if i.hour and i.minute else ''
        s['lng']=i.lng
        s['lat']=i.lat
        s['count']=1
        mpoints.append(a)
        points.append(s)
    return render(request, 'map/accidents.html', {'mpoints':mpoints,'points':points})