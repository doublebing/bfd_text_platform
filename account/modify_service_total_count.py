__author__ = 'BFD_466'

import MySQLdb
import logging
import redis
import traceback
from nlpshow.settings import *

mysql_conn = MySQLdb.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'], passwd=DATABASES['default']['PASSWORD'], db=DATABASES['default']['NAME'], charset='utf8')
mysql_cursor = mysql_conn.cursor()

r = redis.Redis(host=REDIS_HOSTS, port=REDIS_PORT,db=0)
    
def modify_service_total_count(token,add_count,service_name='',model=''):
    try:
        if service_name=='' and model=='':
            senti_weibo_total_count=r.hget(token,'senti_weibo_total_count')
            senti_weibo_total_count=senti_weibo_total_count+add_count
            r.hset(token,'senti_weibo_total_count',senti_weibo_total_count)
            senti_auto_total_count=r.hget(token,'senti_auto_total_count')
            senti_auto_total_count=senti_auto_total_count+add_count
            r.hset(token,'senti_auto_total_count',senti_auto_total_count)
            senti_news_total_count=r.hget(token,'senti_news_total_count')
            senti_news_total_count=senti_news_total_count+add_count
            r.hset(token,'senti_news_total_count',senti_news_total_count)            
            senti_finance_total_count=r.hget(token,'senti_finance_total_count')
            senti_finance_total_count=senti_finance_total_count+add_count
            r.hset(token,'senti_finance_total_count',senti_finance_total_count)
            keywords_total_count=r.hget(token,'keywords_total_count')
            keywords_total_count=keywords_total_count+add_count
            r.hset(token,'keywords_total_count',keywords_total_count)            
            item_label_total_count=r.hget(token,'item_label_total_count')
            item_label_total_count=item_label_total_count+add_count
            r.hset(token,'item_label_total_count',item_label_total_count)
            media_label_total_count=r.hget(token,'media_label_total_count')
            media_label_total_count=media_label_total_count+add_count
            r.hset(token,'media_label_total_count',media_label_total_count)
            auto_summary_total_count=r.hget(token,'auto_summary_total_count')
            auto_summary_total_count=auto_summary_total_count+add_count
            r.hset(token,'auto_summary_total_count',auto_summary_total_count)
            reputation_get_result_total_count=r.hget(token,'reputation_get_result_total_count')
            reputation_get_result_total_count=reputation_get_result_total_count+add_count
            r.hset(token,'reputation_get_result_total_count',reputation_get_result_total_count)
            text_clf_jd_total_count=r.hget(token,'text_clf_jd_total_count')
            text_clf_jd_total_count=text_clf_jd_total_count+add_count
            r.hset(token,'text_clf_jd_total_count',text_clf_jd_total_count)
            return 1
        if service_name=="sentiment":
            if model=="weibo":
                senti_weibo_total_count=r.hget(token,'senti_weibo_total_count')
                senti_weibo_total_count=senti_weibo_total_count+add_count
                r.hset(token,'senti_weibo_total_count',senti_weibo_total_count)
                return 1
            if model=="auto":
                senti_auto_total_count=r.hget(token,'senti_auto_total_count')
                senti_auto_total_count=senti_auto_total_count+add_count
                r.hset(token,'senti_auto_total_count',senti_auto_total_count)
                return 1
            if model=="news":
                senti_news_total_count=r.hget(token,'senti_news_total_count')
                senti_news_total_count=senti_news_total_count+add_count
                r.hset(token,'senti_news_total_count',senti_news_total_count)
                return 1
            if model=="finance":
                senti_finance_total_count=r.hget(token,'senti_finance_total_count')
                senti_finance_total_count=senti_finance_total_count+add_count
                r.hset(token,'senti_finance_total_count',senti_finance_total_count)
                return 1
        if service_name=="reputation":
            if model=="get_result":
                reputation_get_result_total_count=r.hget(token,'reputation_get_result_total_count')
                reputation_get_result_total_count=reputation_get_result_total_count+add_count
                r.hset(token,'reputation_get_result_total_count',reputation_get_result_total_count)
                return 1
        if server_name == "text_classification":
            if model == "jd":
                text_clf_jd_total_count=r.hget(token,'text_clf_jd_total_count')
                text_clf_jd_total_count=text_clf_jd_total_count+add_count
                r.hset(token,'text_clf_jd_total_count',text_clf_jd_total_count)
                return 1
        if model=="":
            if service_name=="keywords":
                keywords_total_count=r.hget(token,'keywords_total_count')
                keywords_total_count=keywords_total_count+add_count
                r.hset(token,'keywords_total_count',keywords_total_count)
                return 1
            if service_name=="item_label":
                item_label_total_count=r.hget(token,'item_label_total_count')
                item_label_total_count=item_label_total_count+add_count
                r.hset(token,'item_label_total_count',item_label_total_count)
                return 1
            if service_name=="media_label":
                media_label_total_count=r.hget(token,'media_label_total_count')
                media_label_total_count=media_label_total_count+add_count
                r.hset(token,'media_label_total_count',media_label_total_count)
                return 1
            if service_name=="auto_summary":
                auto_summary_total_count=r.hget(token,'auto_summary_total_count')
                auto_summary_total_count=auto_summary_total_count+add_count
                r.hset(token,'auto_summary_total_count',auto_summary_total_count)
                return 1
    except:
        logging.error(traceback.format_exc())
        return 0
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

