#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#--------------------------------------------------------
# Purpose:     Socket Server 
# 
# Author:      ronghuihui
# Created:     2016-09-02
# Version:     0.1
# Copyright:   (c) Hikvision.com 2013
#---------------------------------------------------------

from socket import *
import time


def sendToClient():
    listenerSock = socket(AF_INET, SOCK_STREAM)
    listenerSock.connect(('localhost',7800))
    listenerSock.send("return SUCCESS")
    listenerSock.close()

def serverAccept():

    HOST = ""
    PORT = 5555
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    tcpServer = socket(AF_INET, SOCK_STREAM)
    tcpServer.bind(ADDR)
    tcpServer.listen(5)

    print u"server服务端口 %d 已绑定 ..." % PORT

    while 1:
        print u"server等待连接...\n"
        tcpClient, addr = tcpServer.accept()
        print u"server收到来自", addr, u"的连接请求\n\n"
        
        while 1:
            try:
                data = tcpClient.recv(BUFSIZE)
                if not data:
                    break;
                print u"server收到数据data = ", data
                time.sleep(2)

                sendToClient()

            except Exception, e:
                print e
                break
        tcpClient.close()
    tcpServer.close()



if __name__ == '__main__' :
    serverAccept()