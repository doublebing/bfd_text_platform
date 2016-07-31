# coding:utf-8
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
import requests
from django.http import HttpResponse, HttpResponseRedirect
from nlpshow.settings import *
import json
import simplejson
from django.contrib.auth import authenticate,login,logout
from django import forms



def sentiment_weibo(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content').strip()
    mode = request.POST.get('mode')
    contents = content.split('\n')
    input = []
    res_result = {}
    print mode
    if mode == 'multiple':
        if len(contents) > 0:
            for a in contents:
                if len(a) > 0:
                    input.append(a)
            content = json.dumps(input)
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_weibo'])
        result = getResult(url,params)
        res = {}
        for x in range(len(result)):
            res[contents[x]] = int(result[x]*100)
        #正面结果
        pos_result = sorted(res.items(), key=lambda d: d[1], reverse=True)
        #负面结果
        neg_result = sorted(res.items(), key=lambda d: d[1], reverse=False)

        pos2 = []
        neg2 = []

        for i in xrange(len(pos_result)):
            if i == 5:
                break
            text  = pos_result[i][0]
            weight  = pos_result[i][1]
            if weight > 50:
                pos2.append({"text":text,"weight":str(weight)})

        for i in xrange(len(neg_result)):
            if i == 5:
                break
            text = neg_result[i][0]
            weight = neg_result[i][1]
            if weight < 50:
                neg2.append({"text": text, "weight": str(weight)})

        res_result.update({"pos_result": pos2, "neg_result": neg2})
    elif mode == 'single':
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_weibo'])
        result = getResult(url,params)
        res_result.update({"result": int(result*100)})
    return HttpResponse(json.dumps(res_result), content_type='application/json')

def sentiment_news(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content').strip()
    mode = request.POST.get('mode')
    contents = content.split('\n')
    input = []
    res_result = {}
    print mode
    if mode == 'multiple':
        if len(contents) > 1:
            for a in contents:
                if len(a) > 0:
                    input.append(a)
            content = json.dumps(input)
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_news'])
        result = getResult(url,params)
        print result
        res = {}
        for x in range(len(result)):
            res[contents[x]] = int(result[x]*100)
        #正面结果
        pos_result = sorted(res.items(), key=lambda d: d[1], reverse=True)
        #负面结果
        neg_result = sorted(res.items(), key=lambda d: d[1], reverse=False)

        pos2 = []
        neg2 = []

        for i in xrange(len(pos_result)):
            if i == 5:
                break
            text  = pos_result[i][0]
            weight  = pos_result[i][1]
            if weight > 50:
                pos2.append({"text":text,"weight":str(weight)})

        for i in xrange(len(neg_result)):
            if i == 5:
                break
            text = neg_result[i][0]
            weight = neg_result[i][1]
            if weight < 50:
                neg2.append({"text": text, "weight": str(weight)})

        res_result.update({"pos_result": pos2, "neg_result": neg2})
    elif mode == 'single':
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_news'])
        result = getResult(url,params)
        res_result.update({"result": int(result*100)})
    return HttpResponse(json.dumps(res_result), content_type='application/json')

def sentiment_auto(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content').strip()
    mode = request.POST.get('mode')
    contents = content.split('\n')
    input = []
    res_result = {}
    print mode
    if mode == 'multiple':
        if len(contents) > 1:
            for a in contents:
                if len(a) > 0:
                    input.append(a)
            content = json.dumps(input)
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_auto'])
        result = getResult(url,params)
        print result
        res = {}
        for x in range(len(result)):
            res[contents[x]] = int(result[x]*100)
        #正面结果
        pos_result = sorted(res.items(), key=lambda d: d[1], reverse=True)
        #负面结果
        neg_result = sorted(res.items(), key=lambda d: d[1], reverse=False)

        pos2 = []
        neg2 = []

        for i in xrange(len(pos_result)):
            if i == 5:
                break
            text  = pos_result[i][0]
            weight  = pos_result[i][1]
            if weight > 50:
                pos2.append({"text":text,"weight":str(weight)})

        for i in xrange(len(neg_result)):
            if i == 5:
                break
            text = neg_result[i][0]
            weight = neg_result[i][1]
            if weight < 50:
                neg2.append({"text": text, "weight": str(weight)})

        res_result.update({"pos_result": pos2, "neg_result": neg2})
    elif mode == 'single':
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_auto'])
        result = getResult(url,params)
        res_result.update({"result": int(result*100)})
    return HttpResponse(json.dumps(res_result), content_type='application/json')



def sentiment_finance(request):
    #if request.session.get('token',None) is not None:
    #    token=request.session.get('token',None)
    #else:
    #    token = request.POST.get('token')
    token = request.POST.get('token')
    content = request.POST.get('content').strip()
    mode = request.POST.get('mode')
    contents = content.split('\n')
    input = []
    res_result = {}
    print mode
    if mode == 'multiple':
        if len(contents) > 1:
            for a in contents:
                if len(a) > 0:
                    input.append(a)
            content = json.dumps(input)
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_finance'])
        result = getResult(url,params)
        pos2 = []
        neg2 = []
        pos_result = []
        neg_result = []
        for x in range(len(result)):
            if result[x] == 1:
                pos_result.append(contents[x])
            elif result[x] == -1:
                neg_result.append(contents[x])

        for i in xrange(len(pos_result)):
            if i == 5:
                break
            text = pos_result[i]
            pos2.append({"text":text, "weight": "100"})

        for i in xrange(len(neg_result)):
            if i == 5:
                break
            text = neg_result[i]
            neg2.append({"text": text, "weight":"0"})
        res_result.update({"pos_result": pos2, "neg_result": neg2})
    elif mode == 'single':
        params = {"token": token, "content": content}
        url = '%s/%s' % (BASE_URL, NLP_APIS['sentiment_finance'])
        result = getResult(url,params)
        #if result == 0:
        #    result = 0.5
        #res_result.update({"result": int(result*100)})
        res_result.update({"result": result})
    return HttpResponse(json.dumps(res_result), content_type='application/json')




def getResult(url, params):
    res = requests.post(url, data=params).text
    return dict(eval(res))['result']

