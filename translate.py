#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys

API_TOKEN = 'trnsl.1.1.20160701T114615Z.8d93f970075d479e.3a32dd0081533b2d2257ad4696d1ea8a382a917a'
URL_TRANSLATE_YANDEX = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + API_TOKEN
DETECT_TRANSLATE_YANDEX = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key=' + API_TOKEN + '&hint=en,ru'
RusToEng = 'ru-en'
EngToRus = 'en-ru'

def main(text):
    text = ' '.join(text)
    isLang = detect(text)
    if (isLang != 'error'):
        if (isLang == 'ru'):
            print translate(RusToEng, text)
        else:
            print translate(EngToRus, text)
    else:
        print 'error :('


def detect(text):
    response = urllib2.urlopen(DETECT_TRANSLATE_YANDEX + '&text=' + text)
    data = json.load(response)
    if (data['code'] == 200):
        return data['lang'] # 'en' || 'ru'
    else:
        return 'error'

def translate(lang, text):
    url = URL_TRANSLATE_YANDEX + '&lang=' + lang + '&text=' + text
    response = urllib2.urlopen(URL_TRANSLATE_YANDEX + '&lang=' + lang + '&text=' + text)
    data = json.load(response)
    if (data['code'] == 200):
        return data['text'][0].encode('utf8') # 'translate text'

main(sys.argv[1:])
