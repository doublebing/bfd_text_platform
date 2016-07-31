
import redis
import logging
import traceback
from nlpshow.settings import *

r = redis.Redis(host=REDIS_HOSTS, port=REDIS_PORT,db=0)

def serviceUsed(token):
    try:
        service_count_dict={}
        service_count_dict['senti_count_weibo'] = r.hget(token,'senti_count_weibo')
        service_count_dict['senti_weibo_total_count'] = r.hget(token,'senti_weibo_total_count')
        service_count_dict['senti_count_auto'] = r.hget(token,'senti_count_auto')
        service_count_dict['senti_auto_total_count'] = r.hget(token,'senti_auto_total_count')
        service_count_dict['senti_count_news'] = r.hget(token,'senti_count_news')
        service_count_dict['senti_news_total_count'] = r.hget(token,'senti_news_total_count')
        service_count_dict['senti_count_finance'] = r.hget(token,'senti_count_finance')
        service_count_dict['senti_finance_total_count'] = r.hget(token,'senti_finance_total_count')
        service_count_dict['keywords_count'] = r.hget(token,'keywords_count')
        service_count_dict['keywords_total_count'] = r.hget(token,'keywords_total_count')
        service_count_dict['text_clf_count_jd'] = r.hget(token,'text_clf_count_jd')
        service_count_dict['text_clf_jd_total_count'] = r.hget(token,'text_clf_jd_total_count')
        service_count_dict['item_label_count'] = r.hget(token,'item_label_count')
        service_count_dict['item_label_total_count'] = r.hget(token,'item_label_total_count')
        service_count_dict['media_label_count'] = r.hget(token,'media_label_count')
        service_count_dict['media_label_total_count'] = r.hget(token,'media_label_total_count')
        service_count_dict['auto_summary_count'] = r.hget(token,'auto_summary_count')
        service_count_dict['auto_summary_total_count'] = r.hget(token,'auto_summary_total_count')
        service_count_dict['reputation_get_result_count'] = r.hget(token,'reputation_get_result_count')
        service_count_dict['reputation_get_result_total_count'] = r.hget(token,'reputation_get_result_total_count')
        
        return service_count_dict
    except:
        logging.error(traceback.format_exc())
        return {}

#print serviceUsed('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40')
