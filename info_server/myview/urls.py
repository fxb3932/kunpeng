from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index')
    , path('console.html', views.console, name='console')
    , path('add_connect', views.add_connect, name='add_connect')
    , path('get_connect_group_by', views.get_connect_group_by, name='get_connect_group_by')
    , path('login_index', views.login_index, name='login_index')
    , path('login_in', views.login_in, name='login_in')
    , path('user/login.html', views.user_logout, name='user_logout')
    , path('register_index', views.register_index, name='register_index')
    , path('test_resp', views.test_resp, name='test_resp')
]