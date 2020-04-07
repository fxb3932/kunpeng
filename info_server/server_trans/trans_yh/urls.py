from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('stu', views.stu, name='stu'),
    path('ora', views.ora, name='ora'),
]