# coding=utf-8
import datetime
import json
import uuid
import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as base_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import redis

from account.authority_account import *
from models import userInfo
from modify_password import *
from service_count_used import *
from show_userinfo import *
from nlpshow.settings import *

def update_tel(request):
    #username=request.POST["hidden_username"]
    username = request.session.get( 'username', None )
    logging.error("username: %s" % username)
    if username is None or '' == username or not username:
        return HttpResponseRedirect( '/' )
    tel=request.POST["hidden_tel"]
    logging.error(username + ", " + tel)
    user=User.objects.get(username=username)
    user_info=userInfo.objects.get(user_info_id=user.id)
    logging.error(user_info.id)
    user_info.tel=tel
    user_info.save()
    return show_user(request)


# Create your views here.
def login( request ):
    if request.method == "POST":
        user = authenticate( username = request.POST['username'], password = request.POST['password'] )
        if user is not None:
            if user.is_active:
                auth_login( request, user )
                username = request.POST['username']
                request.session['username'] = username
                token = userInfo.objects.filter( user_info__username = username )[0].token
                request.session['token'] = token
                print "user token:", token
                if token:
                    return render( request, 'developer.html', {"username":username} )
        else:
            messages.error( request, '用户名或密码错误！' )
            return render( request, 'login.html' )
    else:
        return render( request, 'login.html' )

def logout( request ):
    # 删除session
    username = request.session.get( 'username', None )
    token = request.session.get( 'token', None )
    if username is not None:
        del request.session['username']
    if token is not None:
        del request.session['token']
    return HttpResponseRedirect( '/' )
    # return render(request,'index.html')

def register( request ):
    if request.method == "POST":
        # 将用户信息写入数据库
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        checkPassword = request.POST["checkPassword"]
        tel = request.POST["tel"]
        if User.objects.filter( username = username ):
            messages.success( request, '该用户已注册！' )
            return render( request, 'register.html' )
        else:
            if password == checkPassword:
                format = '%Y-%m-%d %H:%M:%S'
                cur_time = datetime.datetime.now()
                delta_time = cur_time + datetime.timedelta( days = 90 )
                start_time = cur_time.strftime( format )
                end_time = delta_time.strftime( format )
                token = uuid.uuid1()
                u = User.objects.create_user( username = username, email = email, password = password )
                u.is_active = True
                u.save()
                info = userInfo( user_info = u, tel = tel, token = token, start_time = start_time, end_time = end_time, create_time = start_time )
                info.save()
                account( token, start_time, end_time )
                set_service_total_count( token )
                # 返回登录页面
                return render( request, 'login.html' )
            else:
                messages.error( request, '登录密码与确认密码不一致！' )
                return render( request, 'register.html' )
    else:
        return render( request, 'register.html' )
    
def find_password( request ):
     if request.method == "POST":
         if request.POST.has_key( 'save' ):
             email = request.POST["email"]
             password = request.POST["password"]
             confirm_password = request.POST["confirm_password"]
             print email
             print password
             print confirm_password
             if check_email( email ) != -1:
                 if password == confirm_password:
                     print 'modify start'
                     username = check_email( email )
                     newuser = User.objects.get( username = username )
                     newuser.set_password( password )
                     newuser.save()
                     print 'modify end'
                     return render( request, 'login.html' )
                 else:
                     messages.error( request, '密码输入不一致，请重新输入！' )
                     return render( request, 'password.html' )
             else:
                 messages.error( request, '邮箱输入不正确！' )
                 return render( request, 'password.html' )
     else:
          return render( request, 'password.html' )
      
def get_userinfo( request, username ):
    user_dict = show_userinfo( username )
    email = user_dict["email"]
    tel = user_dict["tel"]
    token = user_dict["token"]
    token_expiration = user_dict["token_expiration"]
    service_count_dict = serviceUsed( token )
    print 'service_count_dict:', service_count_dict
    if service_count_dict != {}:
        senti_count_weibo = service_count_dict['senti_count_weibo']
        senti_weibo_total_count = service_count_dict['senti_weibo_total_count']
        senti_count_auto = service_count_dict['senti_count_auto']
        senti_auto_total_count = service_count_dict['senti_auto_total_count']
        senti_count_news = service_count_dict['senti_count_news']
        senti_news_total_count = service_count_dict['senti_news_total_count']
        senti_count_finance = service_count_dict['senti_count_finance']
        senti_finance_total_count = service_count_dict['senti_finance_total_count']

        keywords_count = service_count_dict['keywords_count']
        keywords_total_count = service_count_dict['keywords_total_count']
        item_label_count = service_count_dict['item_label_count']
        item_label_total_count = service_count_dict['item_label_total_count']
        media_label_count = service_count_dict['media_label_count']
        media_label_total_count = service_count_dict['media_label_total_count']
        auto_summary_count = service_count_dict['auto_summary_count']
        auto_summary_total_count = service_count_dict['auto_summary_total_count']
        reputation_get_result_count = service_count_dict['reputation_get_result_count']
        reputation_get_result_total_count = service_count_dict['reputation_get_result_total_count']
        # print 'auto_summary_count',auto_summary_count
        return render( request, 'user.html', {"username":username, "email":email, "tel":tel, "token":token, "token_expiration":token_expiration, "senti_count_weibo":senti_count_weibo, "senti_count_auto":senti_count_auto, "senti_count_news":senti_count_news, "senti_count_finance":senti_count_finance, "keywords_count":keywords_count, "item_label_count":item_label_count, "media_label_count":media_label_count, "auto_summary_count":auto_summary_count, "reputation_get_result_count":reputation_get_result_count, "senti_weibo_total_count":senti_weibo_total_count, "senti_auto_total_count":senti_auto_total_count, "senti_news_total_count":senti_news_total_count, "senti_finance_total_count":senti_finance_total_count, "keywords_total_count":keywords_total_count, "item_label_total_count":item_label_total_count, "media_label_total_count":media_label_total_count, "auto_summary_total_count":auto_summary_total_count, "reputation_get_result_total_count":reputation_get_result_total_count} )

def show_user( request ):
    username = request.session.get( 'username', None )
    #usernaze = 'p@bfd.com'
    if username is None or {} is username:
        return render( request, 'index.html' )
    else:
        user_dict = show_userinfo( username )
        if user_dict is None or {} == user_dict:
            return render( request, 'index.html' )
        tel = user_dict["tel"]
        token = user_dict["token"]
        token_expiration = user_dict["token_expiration"]
        email = user_dict["email"]
        service_count_dict = serviceUsed( token )
        print 'service_count_dict:', service_count_dict
        if service_count_dict != {}:
            senti_count_weibo = service_count_dict['senti_count_weibo']
            senti_weibo_total_count = service_count_dict['senti_weibo_total_count']
            senti_count_auto = service_count_dict['senti_count_auto']
            senti_auto_total_count = service_count_dict['senti_auto_total_count']
            senti_count_news = service_count_dict['senti_count_news']
            senti_news_total_count = service_count_dict['senti_news_total_count']
            senti_count_finance = service_count_dict['senti_count_finance']
            senti_finance_total_count = service_count_dict['senti_finance_total_count']
            keywords_count = service_count_dict['keywords_count']
            keywords_total_count = service_count_dict['keywords_total_count']
            item_label_count = service_count_dict['item_label_count']
            item_label_total_count = service_count_dict['item_label_total_count']
            media_label_count = service_count_dict['media_label_count']
            media_label_total_count = service_count_dict['media_label_total_count']
            auto_summary_count = service_count_dict['auto_summary_count']
            auto_summary_total_count = service_count_dict['auto_summary_total_count']
            reputation_get_result_count = service_count_dict['reputation_get_result_count']
            reputation_get_result_total_count = service_count_dict['reputation_get_result_total_count']

            senti_weibo_rest_count = int( senti_weibo_total_count ) - int( senti_count_weibo )
            senti_auto_rest_count = int( senti_auto_total_count ) - int( senti_count_auto )
            senti_news_rest_count = int( senti_news_total_count ) - int( senti_count_news )
            senti_finance_rest_count = int( senti_finance_total_count ) - int( senti_count_finance )
            keywords_rest_count = int( keywords_total_count ) - int( keywords_count )
            item_label_rest_count = int( item_label_total_count ) - int( item_label_count )
            media_label_rest_count = int( media_label_total_count ) - int( media_label_count )
            auto_summary_rest_count = int( auto_summary_total_count ) - int( auto_summary_count )
            reputation_get_result_rest_count = int( reputation_get_result_total_count ) - int( reputation_get_result_count )
            return render( request, 'user.html', {"username":username, "email":email, "tel":tel, "token":token, "token_expiration":token_expiration, "senti_count_weibo":senti_count_weibo, "senti_count_auto":senti_count_auto, "senti_count_news":senti_count_news, "senti_count_finance":senti_count_finance, "keywords_count":keywords_count, "item_label_count":item_label_count, "media_label_count":media_label_count, "auto_summary_count":auto_summary_count, "reputation_get_result_count":reputation_get_result_count, "senti_weibo_total_count":senti_weibo_total_count, "senti_auto_total_count":senti_auto_total_count, "senti_news_total_count":senti_news_total_count, "senti_finance_total_count":senti_finance_total_count, "keywords_total_count":keywords_total_count, "item_label_total_count":item_label_total_count, "media_label_total_count":media_label_total_count, "auto_summary_total_count":auto_summary_total_count, "reputation_get_result_total_count":reputation_get_result_total_count, "senti_weibo_rest_count":senti_weibo_rest_count, "senti_auto_rest_count":senti_auto_rest_count, "senti_news_rest_count":senti_news_rest_count, "senti_finance_rest_count":senti_finance_rest_count, "keywords_rest_count":keywords_rest_count, "item_label_rest_count":item_label_rest_count, "media_label_rest_count":media_label_rest_count, "auto_summary_rest_count":auto_summary_rest_count, "reputation_get_result_rest_count":reputation_get_result_rest_count} )

def show_detail( request ):
    username = request.session.get( 'username', None )
    return render( request, 'detail.html', {"username":username} )
