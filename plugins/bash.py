# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Plugin:
    vk = None
    keys = ['bash', u'цитата', u'баш', u'башорг', 'quote']
    name = 'Bash'
    def __init__(self, vk):
        self.vk = vk
        print(Plugin.name)

    def call(self, msg, is_prefixed):
        r = requests.get('http://bash.im/random') #.replace('<br />', '\n')
        doc = r.text.replace('<br>', '\n')
        quote_list = BeautifulSoup(doc, 'lxml').find_all("div", class_="text")[0]
        quote = ''.join(quote_list)
        #try:
        #quote = quote.encode('latin-1').decode('utf-8')
        #except:
        #    print('Что-то не то либо с башем, либо с моими руками')
        self.vk.respond(msg, {'message': quote})