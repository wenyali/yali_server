#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# CGI处理模块
import cgi 

# 引入时间模块
import time
import sys
from subprocess import call,check_output
import os
from sys import argv

def kill_process_by_name(name):
    cmd = "ps -e | grep %s" % name
    #print(cmd)
    f = os.popen(cmd)
    txt = f.readlines()
    #print(txt)
    if len(txt) == 0:
        pass
    else:
        for line in txt:
            colum = line.split()
            pid = colum[0]
            print(pid)
            cmd2 = "kill -9 %d" % int(pid)
            call(cmd2,shell=True)

def is_python3():
    return sys.version > '3'
    
def start_server_with_port(port):
#    try:
#        kill_process_by_name("Python")
#    except:
#        call("echo '\033[31m service open failed \033[0m'",shell=True)

    if is_python3():
        call(["python3","-m","http.server","--cgi",port])
    else:
        call(["python","-m","CGIHTTPServer",port])


def index():
    args = argv
    if (len(args) == 3) and (args[1] == "-port") and (args[2].isdigit()):
        call("echo '\033[32m 服务开启.... \033[0m'",shell=True)
        start_server_with_port(args[2])
    else:
        call("echo '\033[31m usage error\n usage example:\n yaliserver -port 8800 \033[0m'",shell=True)









