#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import re

translateText = 'table'
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
link = "https://www.bing.com/translator/api/Dictionary/Lookup?from=en&to=ru&text=" + translateText
request = urllib2.Request(link, headers=headers)
response = urllib2.urlopen(request).read()
results = json.loads(response)

# print "Translate: {} from {} -> to {}".format(results['originalText'], results['from'], results['to'])

translates = results['items'][0]
for translate in translates:
    noun = round((translate['confidence'] * 100), 0)
    text = translate['normalizedTarget'].encode('utf8')
    print '{:>4}% {}'.format(noun, text)
