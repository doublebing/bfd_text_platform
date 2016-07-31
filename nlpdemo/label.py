# coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import requests
from django.http import HttpResponse, HttpResponseRedirect
from nlpshow.settings import *
import json
import simplejson
from django import forms
import newscrawler
import logging, time, hashlib
import utils
import copy


def crawle_news(request):
    url = ''
    crawler_result = ''
    try:
        url = request.POST.get('url')
        crawler_result = newscrawler.getNewsContent("192.168.80.44",8989, url ,crawler_result)
    except Exception:
        ret_value = copy.deepcopy(utils.RET_FORMAT_ERROR)
        ret_value.update({"msg":"当前url无效"})
        return utils.rep(ret_value)
    ret_value = copy.deepcopy(utils.RET_OK)
    content = crawler_result.split("$$")
    content_data = content[2]
    title_data = content[1]
    if content_data and (content_data != 'null'):
        ret_value.update({"result": content_data, "status":"1"})
    else:
        ret_value.update({"result": content_data, "status":"10","msg":"该页面无内容或未提取出内容"})
    if title_data and (title_data != 'null'):
        ret_value.update({"title": title_data, "status":"1"})
    else:
       ret_value.update({"title": title_data, "status" : "10","msg":"该页面无内容或未提取出内容"})
   
    return utils.rep(ret_value)


def media_label(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content')
    num = request.POST.get('num')
    res_result={}
    if content:
        pass
    else:
	res_result.update({"status":"11","msg":"该页面无内容或未提取出内容"})
        return HttpResponse(json.dumps(res_result), content_type='application/json')
    params = {"token": token, "content": content, "numWords": num}
    url = '%s/%s' % (BASE_URL, NLP_APIS['media_label'])
    res = requests.post(url, data=params).text
    result = simplejson.loads(res)
    result_data = result['result'][0]
    print result_data
    kwords = result_data['keywords']
    print kwords
    sorted_keywords = sorted(kwords.items(), key=lambda d:d[1], reverse=True)
    kw = []
    for i in sorted_keywords:
        kw.append(i[0])
    res_result.update({"keywords": kw, "category": result_data['category'],"status":"0"})
    print res_result
    return HttpResponse(json.dumps(res_result), content_type='application/json')



def item_label(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content')
    title = request.POST.get('title')
    res_result = {}
    if title:
        pass
    else:
        res_result.update({"status":"11","msg":"该页面无内容或未提取出内容"})
        return HttpResponse(json.dumps(res_result), content_type='application/json')
    params = {"token": token, "title": title}
    url = '%s/%s' % (BASE_URL, NLP_APIS['item_label'])
    res = requests.post(url, data=params).text
    result = simplejson.loads(res)
    result_data = result['result']
    print result_data
    if 'category_name_new' in result_data:
        print result_data['category_name_new']
        res_result['category'] = result_data['category_name_new']
    if 'attr' in result_data:
        attr_data = json.loads(result_data['attr'])
        attrdata ={}
        for k, v in attr_data.items():
            attrdata[k] = v[0]
        res_result['attr'] = attrdata
    if 'brand_name_new' in result_data:
        res_result.update({"brand": result_data['brand_name_new']})
    return HttpResponse(json.dumps(res_result), content_type='application/json')
