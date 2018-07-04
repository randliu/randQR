#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from hashlib import sha256
import json
import qrcode
import os


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

    ret.data['content'] = qrstring

    h = sha256()
    h.update(qrstring.encode('utf-8'))
    res = h.hexdigest()
    ret.data['hash'] = res
    ret.data['qr_url'] = "/static/{}.png".format(ret.data['hash'])
    img_qr = qrcode.make(qrstring)

    img_qr_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"img_qr")
    img_qr.save(os.path.join(img_qr_dir,"{}.png".format(ret.data['hash'])))

    s = json.dumps(ret, default=ret_2_json)

    return HttpResponse(s)
