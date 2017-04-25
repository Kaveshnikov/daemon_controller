#!/usr/bin/env python

import aiohttp_jinja2
import jinja2
import os
import sys
import logging

from aiohttp import web
from util import getStatus
from util import execute
from util import getData

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''Помещаем запись в PYTHONPATH'''
sys.path.append(project_root)

'''Обработчик главной страницы'''
@aiohttp_jinja2.template('index.html')
async def index(request):
    status = getStatus(SERVICE)
    service = SERVICE.decode('utf-8')

    return {
        'service': service,
        'status': status
    }

'''Обработчик команд'''
async def command_handler(request):
    command = getData(request)

    if command:
        execute(SERVICE, command)

    status = getStatus(SERVICE)
    return web.Response(text=status)

async def turn(request):
    condition = getData(request)

    if condition:
        file = open(CONDITION, 'w')
        file.write(condition.decode('utf-8'))
    return web.Response()

'''Название сервиса'''
SERVICE = b'ntp'

'''Файл для хранения состояния флажка'''
CONDITION = 'condition.txt'

app = web.Application()

app.router.add_get('/', index, name='index')
app.router.add_post('/', command_handler, name='execute')
app.router.add_post('/turn_on', turn, name='turn_on')

app.router.add_static('/static/',
                      path=str(project_root+'/static'),
                      name='static')

aiohttp_jinja2.setup(
    app, loader=jinja2.PackageLoader('simple_aiohttp_daemon_controller', 'templates'))

web.run_app(app, host='127.0.0.1', port=8080)