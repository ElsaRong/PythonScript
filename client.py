#-*-coding:utf-8
import threading
import time
from socket import *


lCallback = {}
iFuncId = 0


def MyCallback():
    print "MyCallback()\n"; 
    global iFuncId
    global lCallback
    lCallback[iFuncId] = MyCallback
    listener = socket(AF_INET, SOCK_STREAM)
    listener.connect(('localhost', 5555))
    listener.send("[%d] %s [%d]" % (iFuncId, "t1", 2))
    iFuncId += 1


#请求Server建立socket
def requestConnect(callback, cmd, argv):
    global iFuncId
    global lCallback
    lCallback[iFuncId] = callback
    listener = socket(AF_INET, SOCK_STREAM)
    listener.connect(('localhost', 5555))
    doSomething()
    doSomething()
    doSomething()
    listener.send("[%d] %s [%d]" % (iFuncId, cmd, argv))
    listener.close()
    iFuncId += 1

def doSomething():
    print "......"   

def StartListener():
    global iFuncId
    global lCallback
    HOST = ""
    PORT = 7800
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while 1:
        tcpCliSock, addr = tcpSerSock.accept()
        while 1:
            try:
                data = tcpCliSock.recv(BUFSIZE)
                if not data:
                    break
                print 'listener recv = %s' % data
                func = lCallback.get(1,MyCallback)
                print "func=", func
                if func:
                    func()
                    del lCallback[iFuncId]
            except Exception,e:
                print e
                break
        tcpCliSock.close()
    tcpSerSock.close()         
    
if __name__ == '__main__':
    t = threading.Thread(target=StartListener)
    t.setDaemon(True)
    t.start()
    doSomething()
    doSomething()
    requestConnect(MyCallback, "t1", 1)          
    i=0
    while i<20:
        i+=1
        doSomething()
        try:
            time.sleep(0.5)
        except Exception, e:
            print e
            break
    print "----------------------Round--------------------"
