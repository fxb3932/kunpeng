from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json

# import sys
# sys.path.append('server_aiops')


from search_problem.models import info
from search_problem.models import info_stat
from search_problem.models import info_channel
from search_problem.models import info_type,info_comments


from django.forms.models import model_to_dict

import time
from django.db.models import Q


@csrf_exempt
def search_problem(request):
    print('start index search_problem_info')

    print(request.POST)

    search_info_data = info.objects.all()
    info_comments_data = info_comments.objects.all()

    start_date = request.POST.get('start_date')
    if start_date != None and start_date != '':
        search_info_data = search_info_data.filter(update_date__gte=start_date)
        info_comments_data = info_comments_data.filter(update_date__gte=start_date)

    end_date = request.POST.get('end_date')
    if end_date != None and end_date != '':
        search_info_data = search_info_data.filter(update_date__lte=end_date)
        info_comments_data = info_comments_data.filter(update_date__lte=end_date)





    # 搜索
    comm_i_search = request.POST.get('comm_i_search')
    if comm_i_search != None and comm_i_search != '':
        for line in comm_i_search.split(' '):
            search_info_data = search_info_data.filter(
                Q(title__icontains=line)
                | Q(problem_info__icontains=line)
                | Q(problem_answer__icontains=line)
                | Q(trans_code__icontains=line)
                | Q(trans_err__icontains=line)
                # 评论查询？？？
                # | Q(t_comments__name__icontains=line)
            )


    # 0-已录入未解答 1-已解答 2-问题退回审核中 3-新解答审核中
    comm_i_info_stat = request.POST.get('comm_i_info_stat')
    if comm_i_info_stat != None and comm_i_info_stat != '':
        search_info_data = search_info_data.filter(t_stat__stat_id=comm_i_info_stat)

    comm_i_info_channel = request.POST.get('comm_i_info_channel')
    if comm_i_info_channel != None and comm_i_info_channel != '':
        search_info_data = search_info_data.filter(t_channel__code=comm_i_info_channel)

    comm_i_info_type = request.POST.get('comm_i_info_type')
    if comm_i_info_type != None and comm_i_info_type != '':
        search_info_data = search_info_data.filter(t_type__code=comm_i_info_type)

    comm_i_info_check_flag = request.POST.get('comm_i_info_check_flag')
    if comm_i_info_check_flag != None and comm_i_info_check_flag != '':
        search_info_data = search_info_data.filter(info_check_flag=comm_i_info_check_flag)

    comm_i_info_check_flag = [
        {'code': 0, 'name': '未认证'}
        , {'code': 1, 'name': '已认证'}
    ]

    comm_i_info_check_update = request.POST.get('comm_i_info_check_update')
    if comm_i_info_check_update != None and comm_i_info_check_update != '':
        search_info_data = search_info_data.filter(info_check_update=comm_i_info_check_update)

    comm_i_info_check_update = [
        {'code': 0, 'name': '无新评论'}
        , {'code': 1, 'name': '有新评论'}
    ]



    t1 = time.time()

    # info_data = []
    # for line in search_info_data.all():
    #     # 源码函数声明：def model_to_dict(instance, fields=None, exclude=None):
    #     # 其中参数instance是对象实例，fields是指定需要哪些字段，exclude是指定排除哪些字段，exclude比fields优先级高。
    #     dict_data = model_to_dict(line, exclude=[
    #         'input_date'
    #         , 'answer_date'
    #         , 'update_date'
    #         , 'comments_update_date'
    #         , 't_comments'
    #     ])
    #     # print(line.input_date)
    #
    #     try: info__channel_name = line.t_channel.name
    #     except: info__channel_name = ''
    #
    #     try: info__type_name = line.t_type.name
    #     except: info__type_name = ''
    #
    #     dict_data = dict(dict_data, **{
    #         'input_date': str(line.input_date)
    #         , 'answer_date': str(line.answer_date)
    #         , 'update_date': str(line.update_date)
    #         , 't_stat_id': line.t_stat.stat_id
    #         , 't_stat_name': line.t_stat.stat_name
    #         , 'info__channel_name': info__channel_name
    #         , 'info__type_name': info__type_name
    #         , "count_sum": line.count_search + (line.count_chick * 10)
    #
    #
    #     })
    #     info_data.append(dict_data)

    t2 = time.time()
    t = (t2 - t1) * 1000
    print('use time : ' + str(int(t)))

    comm_i_info_stat = []
    for line in info_stat.objects.all():
        comm_i_info_stat.append(model_to_dict(line))

    comm_i_info_channel = []
    for line in info_channel.objects.all():
        comm_i_info_channel.append(model_to_dict(line))

    comm_i_info_type = []
    for line in info_type.objects.all():
        comm_i_info_type.append(model_to_dict(line))

    data = []
    for line in search_info_data.all():

        # try: info__channel_name = line.t_channel.name
        # except: info__channel_name = ''
        # print(line.t_stat.stat_id)
        t_stat = {}
        for line_stat in comm_i_info_stat:
            if line_stat.get('id') == line.t_stat_id:
                t_stat = {
                    "code": line_stat.get('stat_id')
                    , "name": line_stat.get('stat_name')
                }

        t_channel = {}
        for line_sub in comm_i_info_channel:
            if line_sub.get('id') == line.t_channel_id:
                t_channel = {
                    "code": line_sub.get('code')
                    , "name": line_sub.get('name')
                }

        t_type = {}
        for line_sub in comm_i_info_type:
            if line_sub.get('id') == line.t_channel_id:
                t_type = {
                    "code": line_sub.get('code')
                    , "name": line_sub.get('name')
                }

        # problem_answer = BeautifulSoup(line.problem_answer, 'html.parser')
        #         , problem_answer=problem_answer.get_text()
        data.append({
            "id": line.id
            , "title": line.title
            , "trans_code": line.trans_code
            , "trans_err": line.trans_err
            , "problem_info": line.problem_info
            , "problem_answer": line.problem_answer
            , 'problem_answer_txt': line.problem_answer_txt
            , "bank_id": line.bank_id
            , "bank_oper": line.bank_oper
            , "problem_source": line.problem_source
            , "input_oper": line.input_oper
            , "assign_oper": line.assign_oper
            , "answer_oper": line.answer_oper
            , "update_oper": line.update_oper
            , "update_chk_oper": line.update_chk_oper
            , "t_stat_id": t_stat.get('code')
            , "t_stat_name": t_stat.get('name')
            , "info__channel_name": t_channel.get('name')
            , "info__type_name": t_type.get('name')
            , "info_check_flag": line.info_check_flag
            , "info_check_update": line.info_check_update
            , "count_search": line.count_search
            , "count_chick": line.count_chick
            , "input_date": str(line.input_date)
            , "answer_date": str(line.answer_date)
            , "update_date": str(line.update_date)
            , "comments_update_date": str(line.comments_update_date)

            # , "answer_date": line.answer_date.strftime("%Y-%m-%d %H:%M:%S")
            # , "update_date": line.update_date.strftime("%Y-%m-%d %H:%M:%S")
            # , "comments_update_date": line.comments_update_date.strftime("%Y-%m-%d %H:%M:%S")

            , "count_sum": line.count_search + (line.count_chick * 10)

        })

    t1 = t2
    t2 = time.time()
    t = (t2 - t1) * 1000
    print('use time : ' + str(int(t)))

    # 批量同步答复信息
    # for line in info.objects.all():
    #     r = info.objects.get(id=line.id)
    #     print(r.problem_answer)
    #     problem_answer = BeautifulSoup(line.problem_answer, 'html.parser')
    #     r.problem_answer_txt = problem_answer.get_text()
    #     r.save()

    comments_data = []
    for line in info_comments_data.all():
        comments_data.append({
            'update_oper': line.update_oper
            , 'update_date': str(line.update_date)
        })



    resp = {
        'code': 0
        , 'data': data
        , 'comm_i_search': '搜索内容            '
        , 'comm_i_info_stat': comm_i_info_stat
        , 'comm_i_info_channel': comm_i_info_channel
        , 'comm_i_info_type': comm_i_info_type
        , 'comm_i_info_check_flag': comm_i_info_check_flag
        , 'comm_i_info_check_update': comm_i_info_check_update
        , 'comments_data': comments_data
        # , 'new_data': data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
