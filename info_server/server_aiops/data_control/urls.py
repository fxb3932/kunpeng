from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('get_file_info/', views.get_file_info, name='get_file_info'),
    path('data_put/', views.data_put, name='data_put'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]