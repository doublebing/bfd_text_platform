__author__ = 'BFD_466'

import MySQLdb
import logging
import traceback
from nlpshow.settings import *

mysql_conn = MySQLdb.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'], passwd=DATABASES['default']['PASSWORD'], db=DATABASES['default']['NAME'], charset='utf8')
mysql_cursor = mysql_conn.cursor()

def check_email(email):
    try:
        sql="select username from auth_user where email='%s'" % email
        mysql_cursor.execute(sql)
        user_name=mysql_cursor.fetchone()
        user_name=user_name[0]
        if user_name is None:
            return -1
        else:
            return user_name
    except:
        logging.error(traceback.format_exc())
        return -1
def modify_password(email,password):
    try:
        username=check_email(email)
        print 'modifing......'
        sql="update auth_user set password='%s' where username='%s'" % (password,username)
        mysql_cursor.execute(sql)
        mysql_conn.commit()
        print 'returning.....'
        return 1
    except:
        logging.error(traceback.format_exc())
        return 0
