from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('monitor', views.monitor, name='monitor'),
    path('picCvt', views.picCvt, name='picCvt'),


    # 数据获取URL
    path('get_M1_TransTot', views.get_M1_TransTot, name='get_M1_TransTot'),   #获取交易总量
    path('get_M2_TransAmt', views.get_M2_TransAmt, name='get_M2_TransAmt'),   #获取交易总量
    path('get_L1_TransChnlMin', views.get_L1_TransChnlMin, name='get_L1_TransChnlMin'),   #获取交易总量
    path('get_L2_TransWeek', views.get_L2_TransWeek, name='get_L2_TransWeek'),  # 获取交易总量
    path('get_L3_TransDayType', views.get_L3_TransDayType, name='get_L3_TransDayType'),  # 获取交易总量
    path('get_R1_TransPlatMin', views.get_R1_TransPlatMin, name='get_R1_TransPlatMin'),  # 获取交易总量
    path('get_R6_TransTop10', views.get_R6_TransTop10, name='get_R6_TransTop10'),  # 获取交易总量
    path('get_R5_TransTopHD', views.get_R5_TransTopHD, name='get_R5_TransTopHD'),  # 获取交易总量
    path('get_R2_TransComHis', views.get_R2_TransComHis, name='get_R2_TransComHis'),  # 获取交易总量
    path('get_R4_TransPlatRate', views.get_R4_TransPlatRate, name='get_R4_TransPlatRate'),  # 获取交易总量
    path('get_R3_TransChnlBX', views.get_R3_TransChnlBX, name='get_R3_TransChnlBX'),  # 获取交易总量
    path('get_yh_data', views.get_yh_data, name='get_yh_data'),  # 获取交易总量

]