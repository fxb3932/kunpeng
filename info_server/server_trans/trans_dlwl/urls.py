from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post_data/aa', views.post_data, name='post_data'),
]