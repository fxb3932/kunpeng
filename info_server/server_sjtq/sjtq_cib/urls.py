from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('doSjtq/', views.doSjtqView.as_view(), name='doSjtqView'),
    path('queryShell/', views.queryShellView.as_view(), name='queryShellView'),
    path('showResult/', views.showResultView.as_view(), name='showResultView'),
    path('uploadShell/', views.uploadShellView.as_view(), name='uploadShellView'),
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]