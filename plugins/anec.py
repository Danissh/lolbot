# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Plugin:
    vk = None
    keys = [u'анекдот', 'анек', u'joke', u'шутка']
    name = 'Годный Анек'
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        r = requests.get('http://baneks.ru/random') #.replace('<br />', '\n')
        doc = r.text.replace('<br />', '\n')
        anec = BeautifulSoup(doc, 'lxml').p.string
        try:
            anec = anec.encode('latin-1').decode('utf-8')
        except:
            print('Анек какой-то говняный')
        self.vk.respond(msg, {'message': anec})