# coding=utf-8

import logging
import traceback

import MySQLdb

from nlpshow.settings import *
from django.contrib.auth.models import User
from models import userInfo


_mysql_conn = MySQLdb.connect( host = DATABASES['default']['HOST'], user = DATABASES['default']['USER'], passwd = DATABASES['default']['PASSWORD'], db = DATABASES['default']['NAME'], charset = 'utf8' )
_mysql_cursor = _mysql_conn.cursor()

def select_userid( username ):
    try:
        #sql_user = "select id from auth_user where username='%s'" % username
        #_mysql_cursor.execute( sql_user )
        #user_info = _mysql_cursor.fetchone()
        user_info=User.objects.get(username=username)
        logging.error( "auth_user -> id: %d" % user_info.id )
        #user_id = user_info[0]
        user_id = user_info.id
        return user_id
    except:
        logging.error( traceback.format_exc() )
	logging.error( username )
        return 0

def show_userinfo( username ):
    try:
        user_id = select_userid( username )
        user_basicinfo = {}
        # sql_email="select email from auth_user where id='%d'" % user_id
        # _mysql_cursor.execute(sql_email)
        # email=_mysql_cursor.fetchone()[0]
        # sql_info="select tel,token,end_time from account_userinfo where user_info_id='%d'" % user_id
        ##sql_info = "select tel,token,end_time,email from account_userinfo a left join auth_user b on a.user_info_id = b.id where user_info_id='%d'" % user_id
        ##_mysql_cursor.execute( sql_info )
        ##user_info = _mysql_cursor.fetchone()
        user = User.objects.get(id=user_id)
        user_info = userInfo.objects.get(user_info_id=user_id)
        #tel = user_info[0]
        #token = user_info[1]
        #token_expiration = user_info[2]
        tel=user_info.tel
        token=user_info.token
        token_expiration=user_info.end_time
        email = user.email
        user_basicinfo['email'] = email
        user_basicinfo['tel'] = tel
        user_basicinfo['token'] = token
        user_basicinfo['token_expiration'] = token_expiration
        return user_basicinfo
    except:
        logging.error( traceback.format_exc() )
        return {}

def update_email( username, email ):
    try:
        sql = "update auth_user set email='%s' where username='%s'" % ( email, username )
        _mysql_cursor.execute( sql )
        mysql_conn.commit()
        return 1
    except:
        logging.error( traceback.format_exc() )
        return 0

def update_tel(request):
    try:
        #user_id = select_userid( username )
        #sql = "update account_userinfo set tel='%s' where user_info_id='%d'" % ( tel, user_id )
        #_mysql_cursor.execute( sql )
        #mysql_conn.commit()

        username=request.POST["hidden_username"]
        tel=request.POST["hidden_tel"]
        user_info=User.objects.get(username=username)
        user_info.set_tel(tel)
        user_info.save()
        return 1
    except:
        logging.error( traceback.format_exc() )
        return 0

