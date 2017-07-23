# -*- coding: utf-8 -*-

import os
import sys
import time

from vkplus import VkPlus

import settings

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'   #цвета для терминального текста. Добавлять к строке сначала желаемый цвет, заканчивать строку цветом ENDC

def main():
    path = settings.plugin_path
    cmds = {}
    plugins = {}

    global lastmessid
    lastmessid = 0

    print('LOLbot by akaluth(modded by Peachmage)')

    print('Авторизация в вк...')
    global vk
    vk = VkPlus(settings.vk_login, settings.vk_password, settings.vk_app_id)

    print('Подгружаем плагины...')

    print('---------------------------')

    # Подгружаем плагины
    sys.path.insert(0, path)
    for f in os.listdir(path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            try:
                mod = __import__(fname)
                plugins[fname] = mod.Plugin(vk)
            except:
                print(colors.FAIL+fname+colors.ENDC)
                
    sys.path.pop(0)

    print('---------------------------')
    print('Регистрируем плагины...')

    # Регистрируем плагины
    for plugin in plugins.values():
        try:
            for key in plugin.keys:
                cmds[key] = plugin
        except:
            print(colors.WARNING+'Пропущен плохой плагин '+plugin.name+colors.ENDC)
    print('Приступаю к приему сообщений')

    while True:

        values = {
            'out': 0,
            'offset': 0,
            'count': 20,
            'time_offset': 50,
            'filters': 0,
            'preview_length': 0,
            'last_message_id': lastmessid
        }

        response = vk.api.method('messages.get', values)

        if response['items']:
            lastmessid = response['items'][0]['id']
            for item in response['items']:
                print('> ' + item['body'])
                command(item, cmds)
                vk.markasread(item['id'])  # Помечаем прочитанным

        time.sleep(0.5)


def command(message, cmds):
    if message['body'] == u'':
        return
    words = message['body'].split()
	
    if words[0].lower() in settings.prefixes:
        if len(words) > 1 and words[1].lower() in cmds:
            cmds[words[1].lower()].call(message, True)
    else:
        if words[0].lower() in cmds:
            cmds[words[0].lower()].call(message, False)
        else:
            global vk
            vk.respond(message, {'message': 'Моя тебя не панимат!'})
            time.sleep(3)
            vk.respond(message, {'message': 
'''Ах да, наверное ты не знаешь команды:\n•help(помощь) - список плагинов и команд\n•анекдот(анек, шутка, joke)\n•сиськи(boobs)
•рандом(ранд, random, rand, dice, кубик, ролл, roll) - принимает аргументы - например roll 1 1000. По умолчанию - 1-6
•привет(голос, ку)\n•пока(досвидания)\n•bash(башорг, баш, цитата, quote)'''})


if __name__ == '__main__':
    main()
