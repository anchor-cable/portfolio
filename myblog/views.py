# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'myblog/index.html')

def about(request):
    return render(request, 'myblog/about.html')

def works(request):
    return render(request, 'myblog/works.html')

def appendix(request):
    return render(request, 'myblog/appendix.html')