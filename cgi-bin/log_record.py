#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# CGI处理模块
import cgi 

# 引入时间模块
import time
import sys
from subprocess import call,check_output
import os
import socket
from sys import argv

def is_python3():
    return sys.version > '3'
    
def start_server_with_port(port):
    try:
        cmd1 = "lsof -i:"+port+" | grep Python | cut -d ' ' -f 3"
        pid = check_output(cmd1,shell=True)
        pid = pid.decode().split("\n")[0]
        cmd = "kill -9 %d" % int(pid)
        rc = call(cmd,shell=True)
    except:
        pass
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

    
    # 创建 FieldStorage 的实例化
    form = cgi.FieldStorage()

    # 获取日志数据
    if form.getvalue('log'):
        log_text = form.getvalue('log')
    else:
        log_text = "---------terminal error----------"

    print(log_text)
    with open(time.strftime("%Y-%m-%d",time.localtime(time.time()))+".txt","a+") as f:
        f.write(log_text+"\n")
index()

