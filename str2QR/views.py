#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from hashlib import sha256
import json

class RetMsg(object):
    code = 200
    data = {}
    msg = "OK!"

    def __init__(self):
        self.data = {}



def ret_2_json(ret):
    return {
        'code': ret.code,
        'data':ret.data,
        'msg':ret.msg,
    }


def qr(request):
    qrstring = request.GET.get('qrstring')

    ret = RetMsg()
    if qrstring is None:
        ret.msg = "got None string to qr!"
        ret.code = 400
        s = json.dumps(ret, default=ret_2_json)

        return HttpResponse(s)

    #else:
    ret.data['qr_url'] = "qq.com"
    ret.data['content'] = qrstring

    h = sha256()
    h.update(qrstring.encode('utf-8'))
    res = h.hexdigest()
    ret.data['hash'] = res

    s = json.dumps(ret, default=ret_2_json)

    return HttpResponse(s)
