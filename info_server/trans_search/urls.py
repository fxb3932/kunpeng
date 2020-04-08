from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('postTrans/', views.postTrans, name='postTrans'),
]