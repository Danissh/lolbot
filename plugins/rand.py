# -*- coding: utf-8 -*-

import random


class Plugin:
    vk = None
    keys = [u'рандом', u'ранд', 'random', 'rand', 'dice', u'кубик', u'ролл', 'roll']
    name = 'Рандом'
	
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        args = msg['body'].split()
        num = 0
        if is_prefixed == True:
            offset = 0
        else:
            offset = 1
        try:
            if len(args) > 2-offset and len(args) < 4-offset:
                if args[2-offset] < 0:
                    num = random.randint(int(args[2-offset]), 0)
                else:
                    num = random.randint(0, int(args[2-offset]))
            elif len(args) > 3-offset:
                if int(args[2-offset]) < int(args[3-offset]):
                    num = random.randint(int(args[2-offset]), int(args[3-offset]))
                else:
                    num = random.randint(int(args[3-offset]), int(args[2-offset]))
            else:
                num = random.randint(1, 6)

            self.vk.respond(msg, {'message': str(num)})
        except:
            print('Опять ничисла пихаит :C')
            return
