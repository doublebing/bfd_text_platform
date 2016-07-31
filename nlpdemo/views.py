# coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import requests
import logging, time, hashlib
import utils
import copy
from django.http import HttpResponse, HttpResponseRedirect
from nlpshow.settings import *
import json
import simplejson
from django import forms
import client

LOG = logging.getLogger("nlp_view_log")

def index(request):
    username = request.session.get('username',None)
    return render(request, 'index.html',{"username":username})

def show(request):
    username = request.session.get('username',None)
    return render(request, 'show.html',{"username":username})


def developer(request):
    username = request.session.get('username',None)
    return render(request, 'developer.html',{"username":username})

def test(request):
    return render(request, 'test.html')

def admin(request):
    return render(request, 'admin.html')


#关键字提取
def keywords(request):
    params = {}
    try:
        #if request.session.get('token',None) is not None:
        #    token=request.session.get('token',None)
        #else:
        #    token = request.POST.get('token')
        token = request.POST.get('token')
        content = request.POST.get('content')
        num = request.POST.get('num')
        params = {"token": token, "contents": content, "num": num}
    except Exception:
        ret_value = copy.deepcopy(utils.RET_FORMAT_ERROR)
        return utils.rep(ret_value)
    ret_value = copy.deepcopy(utils.RET_OK)

    url = '%s/%s' % (BASE_URL, NLP_APIS['keywords'])
    res = requests.post(url, data=params).text
    result = dict(eval(res))
    data = []
    for k, v in result['result'].items():
        data.append({"text": k.decode("unicode_escape").encode('UTF-8'), "weight": int(v * 10)})
    ret_value.update({"result":data})
    return utils.rep(ret_value)


#主题提取，自动摘要
def auto_summary(request):
    params = {}
    try:
        #if request.session.get('token',None) is not None:
        #    token=request.session.get('token',None)
        #else:
        #    token = request.POST.get('token')
        token = request.POST.get('token')
        content = request.POST.get('content')
        language = request.POST.get('language')
        params = {"token": token, "text": content, "language": language}
    except Exception:
        ret_value = copy.deepcopy(utils.RET_FORMAT_ERROR)
        return utils.rep(ret_value)
    ret_value = copy.deepcopy(utils.RET_OK)
    url = '%s/%s' % (BASE_URL, NLP_APIS['auto_summary'])
    res = requests.post(url, data=params).text
    res_result = simplejson.loads(res)
    print res_result
    data = res_result['result'].encode('UTF-8')
    ret_value.update({"result":data})
    return utils.rep(data)


def getResult(url,params):
    res = requests.post(url, data=params).text
    return dict(eval(res))['result']



def crawle_weibo(request):
    params = {}
    crawler_result = ''
    try:
        keyword = request.POST.get('keyword')
        crawler = client.Crawler()
        crawler_result = crawler.crawl(keyword)
    except Exception:
        ret_value = copy.deepcopy(utils.RET_CRAWLER_ERROR)
        return utils.rep(ret_value)
    ret_value = copy.deepcopy(utils.RET_OK)
    weibo = simplejson.loads(crawler_result)
    res_result = []
    weibo_content = weibo['msg']
    if 'microBlogs' in weibo_content:
        for blog in weibo_content['microBlogs']:
            if len(blog['content'])>2:
                res_result.append(blog['content'])
    if len(res_result) > 20:
        res_result = res_result[:20]
    if len(res_result) < 1:
        ret_value.update({"code":5,"msg":'抓取内容为空'})
    ret_value.update({"result":res_result})
    return utils.rep(ret_value)


def testapi(request):
    ret_value = copy.deepcopy(utils.RET_OK)
    api = request.POST.get('api')
    params = request.POST.get('params')
    res = requests.post(api, data=params).text

    return utils.rep(ret_value)

