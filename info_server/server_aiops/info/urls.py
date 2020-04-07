from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('test/', views.test, name='test'),
]
