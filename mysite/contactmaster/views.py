from django.shortcuts import render
from .models import System, NormalContact, FaultContact, LargeFaultContact
from django.views.generic import ListView
from django.db.models import Q
import datetime

# Create your views here. 
class SystemList(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('query')
 
        if q_word:
            object_list = System.objects.filter(
                Q(system_name__icontains=q_word) | Q(env__icontains=q_word))
            object_list = update_filed( object_list)
        else:
            object_list = System.objects.all()
            object_list = update_filed( object_list)
        return object_list

def detail(request, system_id):
    system_object = System.objects.get(id=system_id)
    object_list = NormalContact.objects.filter(system_id__exact=system_id)
    return render(request, 'detail.html', {'system_name': system_object.system_name, 'object_list': object_list})


























def update_filed(object_list):
    for val in object_list:
        val.tel = val.tel.replace('0','Emergency(緊急)')
        val.tel = val.tel.replace('1','Critical(致命的)')
        val.tel = val.tel.replace('2','Error(エラー)')
        val.tel = val.tel.replace('3','Warning(警告)')
        val.tel = val.tel.replace('4','Information(情報)')
        val.tel = val.tel.replace('5','notice(通知)')
        val.tel = val.tel.replace(',','<br />')

        val.mail = val.mail.replace('0','Emergency(緊急)')
        val.mail = val.mail.replace('1','Critical(致命的)')
        val.mail = val.mail.replace('2','Error(エラー)')
        val.mail = val.mail.replace('3','Warning(警告)')
        val.mail = val.mail.replace('4','Information(情報)')
        val.mail = val.mail.replace('5','notice(通知)')
        val.mail = val.mail.replace(',','\n')

        val.business_day = val.business_day.replace('0','日')
        val.business_day = val.business_day.replace('1','月')
        val.business_day = val.business_day.replace('2','火')
        val.business_day = val.business_day.replace('3','水')
        val.business_day = val.business_day.replace('4','木')
        val.business_day = val.business_day.replace('5','金')
        val.business_day = val.business_day.replace('6','土')
        val.business_day = val.business_day.replace('7','祝')
        val.business_day = val.business_day.replace(',','\n')

        val.start_date = val.start_date.strftime("%Y/%m/%d %H:%M")

        val.business_hour_stat = val.business_hour_stat.strftime("%H:%M")
        val.business_hour_end = val.business_hour_end.strftime("%H:%M")
        
    return object_list
							
