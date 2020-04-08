from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api_menu/', views.api_menu, name='api_menu'),
    path('api_run/', views.api_run, name='api_run'),
    path('test/<str:api>/', views.api_call, name='api_call')
]
from .apis import helloworld
urlpatterns.append(path('helloworld/', helloworld.helloworld, name='helloworld'))

from .apis import oper
urlpatterns.append(path('oper/', oper.oper, name='oper'))

from .apis import cmdb_info
urlpatterns.append(path('cmdb_info/', cmdb_info.cmdb_info, name='cmdb_info'))
urlpatterns.append(path('cmdb_info/<str:api>/', cmdb_info.update, name='update'))

from .apis import cib_qd_count
urlpatterns.append(path('cib_qd_count/', cib_qd_count.cib_qd_count, name='cib_qd_count'))

from .apis import topfe_trans_search
urlpatterns.append(path('topfe_trans_search/', topfe_trans_search.topfe_trans_search, name='topfe_trans_search'))

from .apis import search_problem
urlpatterns.append(path('search_problem/', search_problem.search_problem, name='search_problem'))

from .apis import search_problem_count
urlpatterns.append(path('search_problem_count/', search_problem_count.search_problem_count, name='search_problem_count'))

from .apis import search_problem_count_v2
urlpatterns.append(path('search_problem_count_v2/', search_problem_count_v2.search_problem_count_v2, name='search_problem_count_v2'))

from .apis import search_problem_grafana
urlpatterns.append(path('search_problem_grafana/', search_problem_grafana.search_problem_grafana, name='search_problem_grafana'))
urlpatterns.append(path('search_problem_grafana/search/', search_problem_grafana.search, name='search'))

from .apis import qq_data_count, qq_data_count_myview_show
urlpatterns.append(path('qq_data_count/', qq_data_count.qq_data_count, name='qq_data_count'))
urlpatterns.append(path('qq_data_count/myview_show/', qq_data_count_myview_show.qq_data_count_myview_show, name='qq_data_count_myview_show'))

from .apis import yh_test
urlpatterns.append(path('yh_test/', yh_test.yh_test, name='yh_test'))


