# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
    keys = [u'сиськи', u'boobs']
    name = 'Случайные сиськи'
	
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        answers = []
        answers.append(u"Сиськи поданы!")
        answers.append(u"Случайные сиськи!")
        answers.append(u"Знакомься, сиськи")

        isphoto = False
        boobs = None

        while isphoto is False:
            values = {
            # owner_id = ид группы
                'owner_id': -73401695,
                'offset': random.randint(1, 1252),
                'count': 1
            }

            boobs = self.vk.api.method('wall.get', values)
            if 'attachments' in boobs['items'][0]:
                if 'photo' in boobs['items'][0]['attachments'][0]:
                    isphoto = True

        boobs_att = boobs['items'][0]['attachments'][0]['photo']

        owner_id = str(boobs_att['owner_id'])
        att_id = str(boobs_att['id'])
        access_key = str(boobs_att['access_key'])

        attachment = 'photo' + owner_id + '_' + att_id + '_' + access_key

        print(attachment)

        self.vk.respond(msg, {'message': random.choice(answers),
            'attachment': attachment})
