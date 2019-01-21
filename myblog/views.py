# Create your views here.

from django.shortcuts import render
from .models import AboutList, WorksList


def index(request):
    return render(request, 'myblog/index.html')


def about(request):
    abouts = AboutList.objects.all()
    return render(request, 'myblog/about.html', {"abouts": abouts})


def works(request):
    works = WorksList.objects.all()
    return render(request, 'myblog/works.html', {"works": works})


def appendix(request):
    return render(request, 'myblog/appendix.html')
