#!/usr/bin/python
#-*- coding: UTF-8 -*-


import os
import sys
import time


def mkdir(path): #创建目录
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print "创建目录",path
        os.makedirs(path)
        return True
    else:
        print "目录存在",path
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

def iF_File_open(fileurl,readm="rU"): #读取文件，返回所有内容
    try:
        file_object = open(fileurl,readm) #使用rU 表示读取时候会把\r \n \r\n 替换为\n
    except:
        print "文件%s 读取失败" %fileurl
        return -1
    try:
        all_text = file_object.read()
    except:
        print "文件%s 读取失败" %fileurl
        file_object.close()
        return -1
    file_object.close()
    return all_text

def conf_read(ftxt,fname="config.cf",dir_list="./"):
    retext = {}
    dir_list2 = "../data/"+fname
    if os.path.exists(dir_list+fname):
        all_the_text = iF_File_open(dir_list+fname)#调用自定义函数iF_File_open获取文件内容
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
        all_the_text = iF_File_open(dir_list2)#调用自定义函数iF_File_open获取文件内容
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
        print "无可用配置文件"
