import rjxf_server.views
from rjxf_server.views import _new_path, isFileOk, _work_path
import os
import glob

# 检查是否允许下发 line 字典中需包括 name 与 ip KEY

def chk_xf_line_stat(rjxf_id, line, pathListName):
    # 提前加入下发前本地验证，已操作过无进行处理
    file_rjxf_resp = _new_path + rjxf_id + '_resp/'
    os.chdir(_new_path + rjxf_id)
    pathList = [pathListName]
    file_chk_stat = True
    for line_file in pathList:
        req = {
            "dir": line_file
            , "bank_no": 'NOCHECK'
        }
        if isFileOk(req).get('stat') == True:
            runShellName = line_file + 'add' + line_file.split('/')[1] + '.sh'
            sFileName = file_rjxf_resp + runShellName.split('/')[2] + '_' + line.get('name') + '_' + line.get(
                'ip') + '.resp'
            try:
                f_chk = open(sFileName, 'r')
                lines = f_chk.readlines()
                f_chk.close()
            except FileNotFoundError:
                file_chk_stat = False
                lines = ''
    os.chdir(_work_path)
    return file_chk_stat, lines

def chk_xf_stat(rjxf_id, line):
    # 提前加入下发前本地验证，已操作过无进行处理
    file_rjxf_resp = _new_path + rjxf_id + '_resp/'
    os.chdir(_new_path + rjxf_id)
    pathList = glob.glob('./*/')
    file_chk_stat = True
    for line_file in pathList:
        req = {
            "dir": line_file
            , "bank_no": 'NOCHECK'
        }
        if isFileOk(req).get('stat') == True:
            runShellName = line_file + 'add' + line_file.split('/')[1] + '.sh'
            sFileName = file_rjxf_resp + runShellName.split('/')[2] + '_' + line.get('name') + '_' + line.get(
                'ip') + '.resp'
            try:
                f_chk = open(sFileName, 'r')
                lines = f_chk.readlines()
                f_chk.close()
            except FileNotFoundError:
                file_chk_stat = False
                lines = ''
    os.chdir(_work_path)
    return file_chk_stat, lines

def pathSort(pathList, par):
    tmp_list = []
    for line in pathList:
        if line == par:
            tmp_list.insert(0, line)
        else:
            tmp_list.append(line)
    return tmp_list