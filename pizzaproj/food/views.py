from django.shortcuts import render

from django.http import HttpResponse

from .models import Item

# Create your views here.

def hi(request):
    return HttpResponse("hi this is me")


def model_test(request):
    a = Item.objects.all()
    return render(request, 'index.html', {'a':a})
