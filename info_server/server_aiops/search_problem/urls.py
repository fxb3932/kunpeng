from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('new/new_text_upload/', views.new_text_upload, name='new_text_upload'),
    path('upload/file/', views.upload_file, name='upload_file'),
    path('new/submit/', views.new_submit, name='new_submit'),

    path('search/', views.search, name='search'),

    path('show/<int:info_id>/', views.show, name='show'),
    path('show/<int:info_id>/submit/', views.show_submit, name='show_submit'),
    path('show/<int:info_id>/submit_comments/', views.show_submit_comments, name='show_submit_comments'),
    path('show/<int:info_id>/submit/ok/', views.submit_ok, name='submit_ok'),
    path('show/<int:info_id>/update/', views.show_update, name='show_update'),
    path('show/<int:info_id>/update/submit/', views.show_submit, name='show_submit'),
    path('show/<int:info_id>/update/submit/ok/', views.submit_ok, name='submit_ok'),

    path('list/', views.list, name='list'),
    path('list/get_table_data/', views.get_table_data, name='get_table_data'),

]