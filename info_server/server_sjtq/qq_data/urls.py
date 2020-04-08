from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.index, name='index'),
    # path('upload/upload/', views.upload, name='upload'),
    path('upload/upload/', views.upload_v2, name='upload'),

    path('show/', views.show, name='show'),

    path('myview/show/', views.myview_show, name='myview_show'),

    path('search_problem/show/', views.search_problem_show, name='search_problem_show'),

    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]