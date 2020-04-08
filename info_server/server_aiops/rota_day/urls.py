from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]