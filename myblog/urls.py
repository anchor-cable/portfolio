from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('works/', views.works, name='works'),
    path('appendix/', views.appendix, name='appendix'),
]
