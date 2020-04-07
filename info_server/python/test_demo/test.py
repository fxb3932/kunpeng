# mydict={
#     "results": [
#         {
#             "series": [
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_newmobilefront",
#                         "result": "success",
#                         "server_name": "pubcpweb01"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             9
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_newmobilefront",
#                         "result": "success",
#                         "server_name": "pubcpweb02"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             6
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_posfront",
#                         "result": "failure",
#                         "server_name": "pubcpweb01"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             1
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_posfront",
#                         "result": "success",
#                         "server_name": "pubcpweb01"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             122
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_posfront",
#                         "result": "success",
#                         "server_name": "pubcpweb02"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             127
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_pubcpfront",
#                         "result": "success",
#                         "server_name": "pubcpweb01"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             4
#                         ]
#                     ]
#                 },
#                 {
#                     "name": "event_statistics",
#                     "tags": {
#                         "app_name": "pubcp_pubcpfront",
#                         "result": "success",
#                         "server_name": "pubcpweb02"
#                     },
#                     "columns": [
#                         "time",
#                         "sum"
#                     ],
#                     "values": [
#                         [
#                             "2019-12-20T01:08:00Z",
#                             3
#                         ]
#                     ]
#                 }
#             ]
#         }
#     ]
# }

import json
f = open("/home/insp_ap/tmp/11.log", encoding='utf-8')
mydict = json.load(f)



for line in mydict.get('results')[0].get('series'):
    app_name=line.get('tags').get('app_name')
    result=line.get('tags').get('result')
    server_name=line.get('tags').get('server_name')
    time=line.get('values')[0][0]
    value=line.get('values')[0][1]
    print("app_name:"+app_name+"  result:"+result+"  server_name:"+server_name+"  time:"+time+"  value:"+str(value))


