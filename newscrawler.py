# coding=utf-8  

import sys
sys.path.append('gen-py')
from tutorial import CrawlRemoteServer
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.protocol import TCompactProtocol
import traceback
import time

def getNewsContent(ip, port, url, result):
    try:
        print "IP PORT:" , ip, port
        transport = TSocket.TSocket(ip, port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = CrawlRemoteServer.Client(protocol)
        transport.open()
        result =  client.fetch(url)
        transport.close()
    except Exception as e:
        print "error",e
        traceback.print_exc()
        raise e
    return result




def pythonServerExe(ip, port, url): 
    try:
        print "IP PORT:" , ip, port 
        transport = TSocket.TSocket(ip, port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = CrawlRemoteServer.Client(protocol)  
        transport.open()  
        
        print "predict"
        print client.fetch(url)
        print "\n"

        transport.close() 
    except Exception as e:
        print "error",e
        traceback.print_exc()


def usage():
    print "usage:"
    print "python client_sample.py ip port stringContent"  

