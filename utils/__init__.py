# -*- coding: utf-8 -*-
import json, time, hashlib, os, uuid
from functools import wraps
from django.utils.decorators import available_attrs
from django.http import HttpResponse
import copy
import logging
import json
LOG = logging.getLogger("nlp_view_log")

RET_OK = {"code":0,"msg":"OK"}
RET_FORMAT_ERROR = {"code": 2, "msg": "POST 数据格式错误!"}
WEIBO_ERROR = {"code": 3, "msg": "微博抓取异常"}


def rep(value):
    response = HttpResponse(json.dumps(value))
    response.__setitem__("Content-type", "application/json")
    response.__setitem__("Access-Control-Allow-Origin", "*")
    return response
