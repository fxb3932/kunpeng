from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 可post调用url
import json
from main import connect_mysql


@csrf_exempt
def search_problem_score(request):
    print('start index search_problem_score')

    # 知识库操作记录表数据 搜索、查看、评论
    sql = """
        select a.oper, a.type_id, b.code, b.name, count(*), sum(b.score)
        from search_problem_action a, search_problem_action_type b 
        where 1 = 1 
        and a.type_id = b.id
        and b.code not in(3,4)
        group by a.oper, a.type_id, b.code, b.name
        union
        select a.input_oper, 0, b.code, '录入', count(*), sum(b.score)
        from search_problem_info a, search_problem_action_type b
        where b.code = 3
        group by a.input_oper
        union
        select a.answer_oper, 0, b.code, '解答', count(*), sum(b.score)
        from search_problem_info a, search_problem_action_type b
        where b.code = 4
        group by a.answer_oper ;
    """
    action_data = connect_mysql(sql)

    list_action = []
    for line in action_data:
        list_action.append({
            "first_name": line[0]
            , "code": line[2]
            , "type_name": line[3]
            , "count": line[4]
            , "score": int(line[5])
        })

    m = {}
    for line in list_action:
        first_name = line.get('first_name')

        m.setdefault(first_name, {
            'first_name': first_name
            , 'data': []
        })['data'].append({
            'code': line.get('code')
            , 'type_name': line.get('type_name')
            , 'count': line.get('count')
            , 'score': line.get('score')
        })
    print(m.values())

    data = []
    for line in m.values():
        score_sum = 0
        for line_data in line.get('data'):
            score_sum += line_data.get('score')
        data.append(dict(line, **{
            "score_sum": score_sum
        }))
    #
    #     print(type(line))

    # 录入数据

    # 解答数据

    # 解答被点击数据

    resp = {
        'code': 0
        , 'list_action': list_action
        , 'data': data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")
