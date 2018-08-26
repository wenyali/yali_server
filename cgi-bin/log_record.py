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
    f = os.popen(cmd)
    txt = f.readlines()
    if len(txt) == 0:
        print ("no process \"%s\"!!" % name)
        return
    else:
        for line in txt:
            colum = line.split()
            pid = colum[0]
            cmd = "kill -9 %d" % int(pid)
            rc = os.system(cmd)
            if rc == 0 :
                print ("exec \"%s\" success!!" % cmd)
            else:
                print ("exec \"%s\" failed!!" % cmd)
                return
def is_python3():
    return sys.version > '3'
    
def start_server_with_port(port):
#    try:
#        kill_process_by_name("Python")
#    except:
#        call("echo '\033[31m service open failed \033[0m'",shell=True)
#        pass
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

    current_path=check_output("pwd",shell=True)
    current_path = current_path.decode().split("\n")[0]

    file_name= current_path+"/"+time.strftime("%Y-%m-%d",time.localtime(time.time()))+".txt"
    try:
        with open(file_name,"a+") as f:
            f.write(log_text+"\n")
    except:
        call("echo '\033[32m open fail.... \033[0m'",shell=True)

if __name__ == "__main__":
	index()











