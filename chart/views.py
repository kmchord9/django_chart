from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TempData
# Create your views here.


def index(request):
    return render(request, 'index.html')

def get_data(request):
    labels = ["赤", "青", "黄色", "緑"]

    #, "紫", "橙"
    data = {
        "labels": labels,
        "temp":[d.temp for d in TempData.objects.all()],
        }
    return JsonResponse(data)

def get_day_data(request):
    d = {'date': request.GET.get('date')}
    return render(request, 'index.html', d)
