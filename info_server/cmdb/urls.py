from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('config_bank/', views.config_bank, name='config_bank'),
    path('config_bank/post_config_bank/', views.post_config_bank, name='post_config_bank'),

    # 资产管理 2.0

    # 运维对象录入
    path('cmdb_input/', views.cmdb_input, name='cmdb_input'),

    # 产品管理
    path('cmdb_plat_info/', views.cmdb_plat_info, name='cmdb_plat_info'),
    path('cmdb_plat_info/get_plat_info/', views.get_plat_info, name='get_plat_info'),
]

