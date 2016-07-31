__author__ = 'BFD_466'

import MySQLdb
import logging
import redis
import traceback
from nlpshow.settings import *

mysql_conn = MySQLdb.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'], passwd=DATABASES['default']['PASSWORD'], db=DATABASES['default']['NAME'], charset='utf8')
mysql_cursor = mysql_conn.cursor()

r = redis.Redis(host=REDIS_HOSTS, port=REDIS_PORT,db=0)

'''according to service name,read service_id from tabel service'''
def select_service(service_name):
    try:
        sql_id="select id from service where service_en='%s'" % service_name
        mysql_cursor.execute(sql_id)
        res = mysql_cursor.fetchall()
        return res[0][0]
    except:
        logging.error(traceback.format_exc())
    return 0
def account(token,start_time,end_time):
    try:
        sql_service="insert into userinfo_service(token,service_id,create_time)values(%s,%s,%s)"
        mysql_cursor.executemany(sql_service,[(token,select_service('senti_weibo'),start_time),(token,select_service('senti_auto'),start_time),(token,select_service('senti_news'),start_time),(token,select_service('senti_finance'),start_time),\
                                              (token,select_service('keywords'),start_time),\
                                              (token,select_service('text_clf_jd'),start_time),\
                                              (token,select_service('item_label'),start_time),\
                                              (token,select_service('media_label'),start_time),\
                                              (token,select_service('auto_summary'),start_time),\
                                              (token,select_service('reputation_get_result'),start_time),\
                                              ])
        mysql_conn.commit()

        r.hset(token,'senti_count_weibo','0')
        r.hset(token,'senti_count_auto','0')
        r.hset(token,'senti_count_news','0')
        r.hset(token,'senti_count_finance','0')
        r.hset(token,'keywords_count','0')
        r.hset(token,'text_clf_count_jd','0')
        r.hset(token,'item_label_count','0')
        r.hset(token,'media_label_count','0')
        r.hset(token,'auto_summary_count','0')
        r.hset(token,'reputation_get_result_count','0')
        r.hset(token,'expiration',end_time)
        return 1
    except:
        logging.error(traceback.format_exc())
    return 0
def set_service_total_count(token):
    try:
        default_total_count=r.get('limit_visit_count')
        r.hset(token,'senti_weibo_total_count',default_total_count)
        r.hset(token,'senti_auto_total_count',default_total_count)
        r.hset(token,'senti_news_total_count',default_total_count)
        r.hset(token,'senti_finance_total_count',default_total_count)
        r.hset(token,'keywords_total_count',default_total_count)
        r.hset(token,'text_clf_jd_total_count',default_total_count)
        r.hset(token,'item_label_total_count',default_total_count)
        r.hset(token,'media_label_total_count',default_total_count)
        r.hset(token,'auto_summary_total_count',default_total_count)
        r.hset(token,'reputation_get_result_total_count',default_total_count)
    except:
        logging.error(traceback.format_exc())
if __name__=='__main__':
    REDIS_HOSTS='192.168.80.44'
    REDIS_PORT=6379
    token='1234'
    r = redis.Redis(host=REDIS_HOSTS, port=REDIS_PORT,db=0)   
    r.hset(token,'senti_count_weibo','0')
    r.hset(token,'senti_count_auto','0')
    r.hset(token,'senti_count_news','0')
    r.hset(token,'senti_count_finance','0')
    r.hset(token,'keywords_count','0')
    r.hset(token,'text_clf_count_jd','0')
    r.hset(token,'item_label_count','0')
    r.hset(token,'media_label_count','0')
    r.hset(token,'auto_summary_count','0')
    print 'finish...'

