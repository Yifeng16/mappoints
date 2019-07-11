from django.contrib import admin
from .models import Accident
# Register your models here.
class MapAccidentAdmin(admin.ModelAdmin):
    #list_display = ('ac','year','month','day','date','hour','minute','address','roadtype','text','dead','hurt','weather','rain','wind','naturl','temp','p1_name','p1_birthday','p1_age','p1_id','p1_driveyear','p1_type','p1_dayget','p1_cartype','p1_numoncar','p1_carid','p1_blame','p1_sex','p2_name','p2_birthday','p2_age','p2_id','p2_driveyear','p2_type','p2_dayget','p2_cartype','p2_numoncar','p2_carid','p2_blame','p2_sex','city','lng','lat')
    list_display = ('id','ac','date','address','author')
    list_filter = ('author',)
    search_fields=('ac','text')
    raw_id_fields=('author',)
    ordering=['-id','author']
admin.site.register(Accident,MapAccidentAdmin)