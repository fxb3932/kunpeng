from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('get_info/', views.get_info, name='get_info'),
    path('upload/', views.upload, name='upload'),
    path('delete/', views.delete, name='delete'),
    path('run_mkdir/', views.run_mkdir, name='run_mkdir'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]