from django.urls import path
from . import views
urlpatterns = [
    path('yh_rate', views.index, name='index'),
    path('indextmp', views.indextmp, name='indextmp'),
    path('getData_rateSystem/', views.getData_rateSystem, name='getData_rateSystem'),
    path('getData_rateSystemRange/', views.getData_rateSystemRange, name='getData_rateSystemRange'),
    path('getData_ErrorDetail/', views.getData_ErrorDetail, name='getData_ErrorDetail'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]