from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TempData
import datetime
# Create your views here.


def index(request):
    return render(request, 'index2.html')

def get_data(request):
    if "date" in request.GET:
            data = request.GET.get('date').split('-')
            y = data[0]
            m = data[1]
            d = data[2]

    else:
            dt_now = datetime.datetime.now()
            y = dt_now.year
            m = dt_now.month
            d = dt_now.day

    data = {
        "labels": [d.date for d in TempData.objects.filter(date__year=y, date__month=m, date__day=d)],
        "temp":[d.temp for d in TempData.objects.filter(date__year=y, date__month=m, date__day=d)],
        }
    return JsonResponse(data)

def get_day_data(request):
    #d = {'date': request.GET.get('date')}
    data = request.GET.get('date').split('-')
    y = data[0]
    m = data[1]
    d = data[2]
    return HttpResponse(y+m+d)
