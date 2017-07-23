# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
    keys = [u'приветствие', 'greeting', u'привет', u'голос', u'ку']
    name = 'Приветствия'
	
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        greetings = []

        greetings.append(u'Я - чатбот')
        greetings.append(u'Кекеке')
        greetings.append(u'Запущен и готов служить')
        greetings.append(u'У контакта ужасный флуд-контроль, %username%')
        greetings.append(u'Поцелуйте мой блестящий металлический зад')

        self.vk.respond(msg, {'message': random.choice(greetings)})
