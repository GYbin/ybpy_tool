#!/usr/bin/python
#-*- coding: UTF-8 -*-


import os
import sys
import time
import re
import logging #日志模块
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
'''
导入模块 
import sys
sys.path.append('父目录的路径')
===================================
get_fname(fname,fileurl='./',mode = 0) #fname为列表获取目录文件
mkdir(path) #创建目录
get_time(ms = 0) #获取时间，使用参数获取毫秒级时间戳
file_rall(fileurl,readm="rU") #读取文件，返回所有内容
file_rline(fileurl,readm="r") #读取文件，每次返回一行
conf_read(ftxt,fname="config.cf",dir_list="./") #ftxt为列表，读取文件配置内容
chec_code(content) #content字典类型，各种格式匹配



'''
#sys._getframe().f_back.f_code.co_name #获取调用函数名
#sys._getframe().f_back.f_lineno     #获取行号
#sys._getframe().f_code.co_name # 获取当前函数名


def get_fname(fname,fileurl='./',mode = 0): #获取目录文件
    excfile = []
    info = os.getcwd()
    if fileurl == './':
        listfile = os.listdir(info)
    else:
        listfile = os.listdir(fileurl)
    if mode == 0:
        for tmp in fname:
            try:
                listnum = listfile.index(tmp)
            except:
                logging.info('没找到文件:%s',tmp)
            else:
                excfile.append(listfile[listnum])
                listfile.remove(tmp)
        redata = listfile,excfile
        return redata
    elif mode == 1:
        for tmp in fname:
            listnum = listfile.index(tmp)
            excfile.append(listfile[listnum])
        return excfile
    elif mode == 2:
        return listfile
    else:
        logging.info("get_fname 参数错误")
        return -1

def mkdir(path): #创建目录
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        logging.info("创建目录:%s",path)
        os.makedirs(path)
        return True
    else:
        logging.info("目录存在:%s",path)
        return False

def get_time(ms = 0): #获取时间，输入参数为获取毫秒时间
    ct = time.time()
    local_time = time.localtime(ct)
    if ms == 0:
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return data_head
    else:
        data_head = time.strftime("%Y%m%d%H%M%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        time_stamp = "%s%03d" % (data_head, data_secs)
        return time_stamp

def file_rall(fileurl,readm="rU"): #读取文件，返回所有内容
    try:
        file_object = open(fileurl,readm) #使用rU 表示读取时候会把\r \n \r\n 替换为\n
    except:
        logging.info("文件%s 打开失败",fileurl)
        return -1
    try:
        all_text = file_object.read()
    except:
        logging.info("文件%s 读取失败",fileurl)
        file_object.close()
        return -1
    file_object.close()
    return all_text

def file_rline(fileurl,readm="r"):#读取文件，返回一行
    global ybpy_tool_file_object
    ifbl = 0
    try :
        ybpy_tool_file_object
    except:
        ifbl = 1
    if ifbl:
        #print "打开文件"
        try:
           ybpy_tool_file_object = open(fileurl,readm) #使用rU 表示读取时候会把\r \n \r\n 替换为\n
        except:
            logging.info("文件%s 打开失败",fileurl)
            return -1
    try:
        all_text = ybpy_tool_file_object.readline()
    except:
        logging.info("文件%s 读取失败",fileurl)
        ybpy_tool_file_object.close()
        return -1
    if not all_text:
       # print "删除了文件函数"
        ybpy_tool_file_object.close()
        del ybpy_tool_file_object
        return 0
    return all_text

def conf_read(ftxt,fname="config.cf",dir_list="./"): #读取配置文件
    retext = {}
    dir_list2 = "../data/"+fname
    if os.path.exists(dir_list+fname): #是否存在配置文件，不存在去默认位置查找
        all_the_text = file_rall(dir_list+fname)#调用自定义函数file_rall获取文件内容
        all_text_list = all_the_text.split("\n")
#        print all_text_list
        for name in ftxt:
            name = name.strip()
            for all_text_lines in all_text_list:
                all_text_lists = all_text_lines.split("=")
#                print name,all_text_lists[0]
                if name == all_text_lists[0].strip():
                    retext[name]=all_text_lists[1].strip()
        return retext
    elif os.path.exists(dir_list2):
        all_the_text = file_rall(dir_list2)#调用自定义函数file_rall获取文件内容
        all_text_list = all_the_text.split("\n")
#        print all_text_list
        for name in ftxt:
            name = name.strip()
            for all_text_lines in all_text_list:
                all_text_lists = all_text_lines.split("=")
#                print name,all_text_lists[0]
                if name == all_text_lists[0].strip():
                    retext[name]=all_text_lists[1].strip()
        return retext
    else:
        logging.info("无可用配置文件")

def chec_code(content): #各种格式匹配
    rule = {'email':'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',
            'sfzid18':'^\d{17}[\d|x|X]',
            'sfzid15':'^\d{14}[\d|x|X]',
            'passwd':'^\w[\s|\S]{5,24}$'}
    for yzname in content:
        patter = rule[yzname]
        if not patter:
            logging.info("规则未定义:%s",yzname)
            return -1
        info = re.findall(patter,content[yzname])
        if not info:
            logging.info("匹配失败 %s: %s",yzname,content[yzname])
            return -1
    return 0


