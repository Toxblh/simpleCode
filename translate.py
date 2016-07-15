#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys
import re

API_TOKEN_YANDEX = 'trnsl.1.1.20160701T114615Z.8d93f970075d479e.3a32dd0081533b2d2257ad4696d1ea8a382a917a'
URL_TRANSLATE_YANDEX = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + API_TOKEN_YANDEX
DETECT_TRANSLATE_YANDEX = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key=' + API_TOKEN_YANDEX + '&hint=en,ru'
RusToEng = 'ru-en'
EngToRus = 'en-ru'

def main(text):
    text = ' '.join(text)
    lang = detect(text)
    translateYandex(lang, text)

    textForBing = text.split()
    print textForBing, len(textForBing)
    if (len(textForBing) == 1):
        translateBing(lang, text)
    else:
        for part in textForBing:
            translateBing(lang, part)


def translateBing(lang, text):
    if (lang == 'ru'):
        translateTo = 'from=ru&to=en'
    else:
        translateTo = 'from=en&to=ru'
    translateText = text
    res = urllib2.urlopen('https://www.bing.com/translator/')
    resheaders = str(res.info())
    cookies = re.findall("Set-Cookie: ([^;]*)", resheaders)

    cookAll = ""
    for cookie in cookies:
        cookAll = cookAll + cookie + ';'

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'Cookie': cookAll,
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Host':'www.bing.com',
        'Pragma':'no-cache',
        'Save-Data':'on',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }
    link = "https://www.bing.com/translator/api/Dictionary/Lookup?" + translateTo + "&text=" + translateText
    request = urllib2.Request(link, headers=headers)
    response = urllib2.urlopen(request).read()
    results = json.loads(response)
    translates = results['items'][0]

    print '[Bing]'
    for translate in translates:
        noun = round((translate['confidence'] * 100), 0)
        text = translate['normalizedTarget'].encode('utf8')
        print '{:>8}% {}'.format(noun, text)

def translateYandex(lang, text):
    if (lang != 'error'):
        if (lang == 'ru'):
            translate(RusToEng, text)
        else:
            translate(EngToRus, text)
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
        print '[Yandex]'
        print '    {}'.format(data['text'][0].encode('utf8')) # 'translate text'

main(sys.argv[1:])
