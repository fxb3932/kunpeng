from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_index', views.login_index, name='login_index'),
    path('post/', views.post, name='post'),
    path('abcd/add', views.add_data, name='add_data'),
    path('abcd/add_submit/', views.add_submit, name='add_submit'),
    path('abcd/show', views.showdata1, name='showdata1'),
    path('abcd/show2', views.showdata2, name='showdata2'),
    path('abcd/<int:thing_id>/update', views.update_data, name='update_data'),
    path('abcd/<int:thing_id>/delete', views.delete_data, name='delete_data'),
    path('abcd/<int:thing_id>/query', views.query_data, name='query_data'),
    path('abcd/<int:thing_id>/update_submit', views.update_submit, name='update_submit')
    # path('fxb_test/', views.fxb_test, name='fxb_test'),
]
