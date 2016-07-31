import MySQLdb

mysql_conn=MySQLdb.connect(host='192.168.80.44',user='root',passwd='',db='userinfo_manage',charset='utf8')
mysql_cursor=conn.cursor()
def insert_visit_mysql(token,ip,port,url,visit_time,request_time,request_status,status_desc):
    try:
        sql="insert into visit_user(token,ip,port,url,visit_time,request_time,request_status,status_desc)values('%s','%s',%s,'%s','%s',%s,%s,'%s')" % (token,ip, port, url,visit_time,request_time,request_status,status_desc)
        mysql_cursor.execute(sql)
        mysql_conn.commit()
        return True
    except:
        logging.error(traceback.format_exc())
        return False

if __name__=='__main__':
    insert_visit_mysql('2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40','192.168.80.44','2181','testnlp.baifendian.com/sentiment/weibo','13','23',200,'')
