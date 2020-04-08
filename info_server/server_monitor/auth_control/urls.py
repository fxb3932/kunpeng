from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]