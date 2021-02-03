#! /usr/bin/python3

import os,re

def ip_munber(): #ip 数量统计
    with open(os.getcwd()+'\\host.txt', 'r',encoding='UTF-8') as file:
        fi = file.readlines()
    re_ip = re.compile("[0-9]+(?:\.[0-9]+){3}")
    re_port = re.compile("[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?")
    ip = re.findall(re_ip,str(fi))
    port = re.findall(re_port,str(fi))
    return len(ip)
    

def ip_data(target): #导入数据 ip
    with open(os.getcwd()+'\\host.txt', 'r',encoding='UTF-8') as file:
        fi = file.readlines()
    re_ip = re.compile("[0-9]+(?:\.[0-9]+){3}")
    re_port = re.compile("[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?")
    ip = re.findall(re_ip,str(fi))
    port = re.findall(re_port,str(fi))
    return ip[target]

def port_data(target): #导入数据 port
    with open(os.getcwd()+'\\host.txt', 'r',encoding='UTF-8') as file:
        fi = file.readlines()
    re_ip = re.compile("[0-9]+(?:\.[0-9]+){3}")
    re_port = re.compile("[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?")
    ip = re.findall(re_ip,str(fi))
    port = re.findall(re_port,str(fi))
    return port[target][1:]