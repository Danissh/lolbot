# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
    keys = [u'пока', u'досвидания']
    name = 'Прощания'
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        bye = []

        bye.append(u'Уже уходишь? :(')
        bye.append(u'Ну и катись, раз разговаривать не хочешь.')
        bye.append(u'Буду скучать')
        bye.append(u'А я поговорить хотел(')
        bye.append(u'До встречи!')

        self.vk.respond(msg, {'message': random.choice(bye)})
