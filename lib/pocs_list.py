#! /usr/bin/python3

#poc-game3 一款批量漏洞扫描验证工具 官网：www.poc-game.me

#author by Greekn 
#列出pocs 文件夹中的poc脚本


import os

def pocs_list_number(): # 列出 poc数量
    path = os.getcwd()+'\\pocs\\'
    pocsname = os.listdir(path)
    sl =len(pocsname)
    return sl -1

def pocs_list_name(target): # 列出 poc名称
    path = os.getcwd()+'\\pocs\\'
    pocsname = os.listdir(path)
    return pocsname[target]


    