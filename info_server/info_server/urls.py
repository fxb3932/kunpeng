"""info_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('info.urls')),
    path('', include('myview.urls')),
    path('myview/', include('myview.urls')),
    path('trans_dlzf/', include('trans_dlzf.urls')),
    path('rjxf_server/', include('rjxf_server.urls')),
    path('trans_jrick/', include('trans_jrick.urls')),
    path('trans_yh/', include('trans_yh.urls')),
    path('cmdb/', include('cmdb.urls')),
    path('trans_dlwl/', include('trans_dlwl.urls')),
    path('trans_fxq_report/', include('trans_fxq_report.urls')),
    path('chkpcl_server/', include('chkpcl_server.urls')),
    path('monitor_wx_zfb/', include('monitor_wx_zfb.urls')),
    path('monitor_wx_zfb_DAY/', include('monitor_wx_zfb_DAY.urls')),
    path('monitor_wx_zfb_2/', include('monitor_wx_zfb_2.urls')),
    path('trans_bwpt/', include('trans_bwpt.urls')),
    path('rota_day/', include('rota_day.urls')),
    path('cloud_file/', include('cloud_file.urls')),
    # path('', include('auth_control.urls')),
    path('data_control/', include('data_control.urls')),
    path('chkpcl_V2/', include('chkpcl_V2.urls')),
    path('monitor_xysj_nzjs/', include('monitor_xysj_nzjs.urls')),
    path('monitor_nzjs/', include('monitor_nzjs.urls')),
    path('monitor_nzjs_renhang/', include('monitor_nzjs_renhang.urls')),
    path('monitor_nzjs_szk/', include('monitor_nzjs_szk.urls')),
    path('sjtq_cib/', include('sjtq_cib.urls')),
    path('data_api/', include('data_api.urls')),
    path('search_problem/', include('search_problem.urls')),
    path('trans_zl_helloworld/', include('trans_zl_helloworld.urls')),
    path('topfe_reportform/', include('topfe_reportform.urls')),
    path('monitor_inspection/', include('monitor_inspection.urls')),
    path('qq_data/', include('qq_data.urls')),
    path('rate_system/', include('rate_system.urls'))

]
