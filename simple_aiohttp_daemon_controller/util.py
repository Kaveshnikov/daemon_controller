import subprocess
import logging

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