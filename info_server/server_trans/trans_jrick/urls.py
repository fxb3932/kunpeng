from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('submit_new/', views.submit_new, name='submit_new'),
    path('submit_aa/', views.submit_aa, name='submit_aa'),
    path('submit_bb/', views.submit_bb, name='submit_bb'),

    path('aaa/', views.aaa, name='aaa'),
    path('get_trans/', views.get_trans, name='get_trans'),
]