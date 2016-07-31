#encoding=utf-8
import sys, traceback, Ice, json, time
import com.bfd.crawler

class Crawler(object):
    def crawl(self,keyword):
        status = 0
        ic = None
        try:
            ic = Ice.initialize(sys.argv)
            base = ic.stringToProxy("weiboCrawlService -t:tcp -h 192.168.40.213 -p 20011")
            client = com.bfd.crawler.weiboControlPrx.checkedCast(base)
            if not client:
                raise RuntimeError("Invalid proxy")
            id = str(time.time())
            request = {'keyword_sign':'b140000','keyword_id':id,'keyword':keyword}
            request = json.dumps(request)
            client.addTask(request)
            client.addTask(request)
            query = {'keyword_sign':'b140000','keywords':[{'id':id,'keyword':keyword,'enable':'True'}]}
            query = json.dumps(query)
            result = client.queryTask(query)
            #delstatus = client.delTask(request)
            return result

        except:
            traceback.print_exc()
            status = 1

        if ic:
        # Clean up
            try:
                ic.destroy()
            except:
                traceback.print_exc()
                status = 1
        sys.exit(status)
if __name__ == '__main__':
    c = Crawler()
    result = c.crawl("世界很大")
    print result

