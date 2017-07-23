# -*- coding: utf-8 -*-

import os
import sys


class Plugin:
    vk = None
    keys = [u'help', 'помощь']
    name = 'Help'
	
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        lists = ''
        path = 'plugins/'
        sys.path.insert(0, path)
        for f in os.listdir(path):
            fname, ext = os.path.splitext(f)
            if ext == '.py':
                lists += fname + '\n'
        sys.path.pop(0)
        self.vk.respond(msg, {'message': u'Загруженные плагины:\n' + lists + 'Команды:\n•help(помощь) - список плагинов и команд\n•анекдот(анек, шутка, joke)\n•сиськи(boobs)\n•рандом(ранд, random, rand, dice, кубик, ролл, roll) - принимает аргументы - например roll 1 1000. По умолчанию - 1-6\n•привет(голос, ку)\n•пока(досвидания)\n•bash(башорг, баш, цитата, quote)'})
