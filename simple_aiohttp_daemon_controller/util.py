import subprocess
import logging
import os

PROCESS = '/bin/bash'

'''Возвращает статус сервиса (active/inactive)'''
def getStatus(service):
    command = b'service ' + service + b' status | grep active'
    pipe = subprocess.Popen(PROCESS, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    tpl = pipe.communicate(command)
    arr = tpl[0].strip().split(b' ')
    status = arr[1].decode('utf-8')
    return status

'''Выполняет команду для сервиса (start/stop/restart)'''
def execute(service, command):
    pattern = b'service ' + service + b' '
    pipe = subprocess.Popen(PROCESS, stdin=subprocess.PIPE)
    pipe.communicate(pattern + command)

'''Возвращает данные POST запроса'''
def getData(request):
    deq = request.content._buffer
    data = None

    if len(deq) > 0:
        data = deq.pop()
    else:
        logging.error('Empty POST')

    return data


'''Читает из файла и возвращает состояние флага '''
def getFlag(file):
    try:
        file = open(file, 'r')
    except IOError as ex:
        return False
    else:
        with file:
            flag = file.readline()
            if flag == 'true':
                return True
            elif flag == 'false':
                return False
            else:
                return None
