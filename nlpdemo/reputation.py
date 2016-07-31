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
import string

import random
import demo_data
import demo_result
import logging

logger = logging.getLogger(__name__)

I = 1

def reputation(request):

    logger.info(request.session.get('token'))

    #if request.session.get('token') is not None:
    #    token=request.session.get('token')
    #else:
    #    token = request.POST.get('token')

    token = request.POST.get('token')
    module = request.POST.get('module')
    taskID = 'car_1_1'
    input_data = []
    
    global I
    if I > 3:
       I = 1

    if module == 'car':
        #taskID = random.choice(cars)
        taskID = 'car_1_'+str(I)
        input_data = demo_data.car_data[taskID].split('\n')
        res = demo_result.car_result[taskID]
    elif module == 'mobile':
        taskID = 'mobile_1_'+str(I)
        #taskID = random.choice(mobiles)
        input_data = demo_data.mobile_data[taskID].split('\n')
        res = demo_result.mobile_result[taskID]
    params = {"token": token, "taskID": taskID}
    url = '%s/%s' % (BASE_URL, NLP_APIS['reputation'])

    #res = requests.post(url, data=params).text
    
    I+=1

    #result = simplejson.loads(res)['result']
    result = simplejson.loads(res)

    if 'There is no such data.' == result:
        return HttpResponse(json.dumps({"input_data": input_data, "result":res, "taskID":taskID}), content_type='application/json')

    res_result = {}
    print result
    for k, v in result.items():
        c_cum = v['num']
        if c_cum >1 :
            button_str = "%s(%s)" % (k, str(v['num']))
            contents = []
            for content in v['list']:
                content_str = input_data[int(content[1])]
                content_0 = content[0].encode("utf-8")
                content_data = content_str.replace(content_0, '<span class="icon_red">'+content_0+'</span>')
                contents.append(content_data)
            res_result[button_str] = contents

    return HttpResponse(json.dumps({"input_data": input_data, "result":res_result, "taskID":taskID}), content_type='application/json')

