#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2

def main(argv) :
    if argv[0] == 'decode':
        out = urldecode(argv[1])
    else:
        out = urlencode(argv[1])
    print out

def urlencode(s):
    return urllib2.quote(s)

def urldecode(s):
    return urllib2.unquote(s)

main(sys.argv[1:])
