from django.urls import path
from . import views
urlpatterns = [
    path('make/', views.make, name='make'),
    path('make/upload/', views.upload, name='upload'),
    path('make/submit/', views.submit, name='submit'),
    path('make/post_tree/', views.post_tree, name='post_tree'),
    path('show/', views.show, name='show'),
    path('show/get/', views.show_get, name='show_get'),
    path('release/', views.release, name='release'),
    path('release/post_rjxffw_table_data/', views.post_rjxffw_table_data, name='post_rjxffw_table_data'),
    path('release/post_xf_command/', views.post_xf_command, name='post_xf_command'),
    path('release/post_resp/', views.post_resp, name='post_resp'),

    path('release/post_xf_stat/', views.post_xf_stat, name='post_xf_stat'),
    path('release/post_chk_stat/', views.post_chk_stat, name='post_chk_stat'),
    path('release/post_chk_passwd/', views.post_chk_passwd, name='post_chk_passwd'),

    # 公共调用模块
    path('get_rjxf_file_info/', views.get_rjxf_file_info, name='get_rjxf_file_info'),
    path('make/post_get_tree_list/', views.post_get_tree_list, name='post_get_tree_list'),


    #测试使用
    path('test/', views.test, name='test'),
    path('fxb_test/', views.fxb_test, name='fxb_test'),
]