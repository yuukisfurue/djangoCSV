from django.urls import path
from . import views
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Guest
from django.views.generic import ListView
from django.views.generic import DetailView

import csv

class GuestList(ListView):
    model = Guest

class GuestDetail(DetailView):
    model = Guest

def index(request, num=1):
    data = Guest.objects.all()
    page = Paginator(data, 8)
    params = {
        'title': 'Admin',
        'message':'',
        'data': page.get_page(num),
    }
    return render(request, 'admin/index.html', params)

def csv_export(request):
	filename='export.csv'
	response = HttpResponse(content_type='text/csv;charset=utf_8_sig')
	response['Content-Disposition'] = "attachment;  filename='{}'; filename*=UTF-8''{}".format(filename, filename)

	w = csv.writer(response)
	w.writerow(['id','name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','potion','annual','lastyear'])
	    
	data = Guest.objects.all()
	for item in data:
		w.writerow([item.id, item.name, item.prefecture, item.gender, item.employmentstatus,item.company, item.jyob, item.stay, item.affiliation, item.postion, item.annual, item.lastyear])
	return response