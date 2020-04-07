from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('yh_echart_demo', views.yh_echart_demo, name='yh_echart_demo'),
    path('demo.html', views.demo, name='demo'),

    path('post_V2pcl', views.post_V2pcl, name='post_V2pcl'),

]