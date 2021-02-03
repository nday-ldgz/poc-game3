#! /usr/bin/python3

#poc-game3 一款批量漏洞扫描验证工具 

#time 2021-1-10 PM 21:31

#author by Greekn 

#tag 有点烦

import sys,importlib,threading,click,os,time
from pyunit_color import FontColor
from iupdatable.logging.Logger import Logger
from iupdatable.logging.LogLevel import LogLevel
from iupdatable.system.io.File import File

Logger.get_instance().config(log_level=LogLevel.DEBUG) #开启日志监控  设置为 DEBUG，输出所有信息 设置为 WARNING, INFO、 级别的日志就不会输出

icobanner = '''
 _____   _____   _____        _____       ___       ___  ___   _____   _____  
|  _  \ /  _  \ /  ___|      /  ___|     /   |     /   |/   | | ____| |___  | 
| |_| | | | | | | |          | |        / /| |    / /|   /| | | |__      _| | 
|  ___/ | | | | | |          | |  _    / / | |   / / |__/ | | |  __|    |_  { 
| |     | |_| | | |___       | |_| |  / /  | |  / /       | | | |___   ___| | 
|_|     \_____/ \_____|      \_____/ /_/   |_| /_/        |_| |_____| |_____/ 

poc-game3 一款批量漏洞扫描验证工具 

当前版本：V1.0.0

'''

@click.group()
def main():
 pass

@main.command()
@click.option('-p', '--poclist', type=str, help='列出全部POC输入命令：pocs_list')
def poc_game3_pocs(poclist):# pocs仓库 初始化
    pocs_initialize = importlib.import_module('lib.'+poclist) #获取pocs 仓库列表
    try:
        #print(pocs_initialize.pocs_list_data())
        Logger.get_instance().info('[+]加载初始化Pocs仓库......')
        Logger.get_instance().info('[+]当前Poc数量:'+str(pocs_initialize.pocs_list_number()))
        #Logger.get_instance().info('[+]列出Pocs仓库名称:'+str(pocs_initialize.pocs_list_name(2)))
        for i in range(pocs_initialize.pocs_list_number()):
            Logger.get_instance().info('[+]['+str(i)+']列出Pocs名称:'+str(pocs_initialize.pocs_list_name(i)))
    except:
        Logger.get_instance().error('[-]pocs仓库初始化报错......！')

@main.command()
@click.option('-n', '--number', type=str, help='查看IP数量：ip_load_target')
def poc_game3_ipnumber(number): #查看ip数量
    ip_target = importlib.import_module('lib.'+number)
    try:
        Logger.get_instance().info('[+]查看host.txt文本IP数量......')
        Logger.get_instance().info('[+]加载ip数据中......')
        Logger.get_instance().info('[+]当前ip数量:'+str(ip_target.ip_munber()))
        #ip_target.ip_data(1) ip
        #port_data(1) port
    except:
        Logger.get_instance().error('[-]查看ip数量报错......！')


@main.command()
@click.option('-v', '--vulnerabilityinfo', type=str, help='查看POC模块信息：请输入POC模块名称')   
def poc_game3_pocinfo(vulnerabilityinfo): #查看POC模块信息
    pocs_load = importlib.import_module('pocs.'+vulnerabilityinfo)
    try:
        Logger.get_instance().info(pocs_load.vulnerability_info())
    except:
        Logger.get_instance().error('[-]查看POC模块信息报错......！')
        
        
@main.command()
@click.option('-o', '--only', type=str, help='POC单一检测模式：请输入POC模块名称')
@click.option('-t', '--target', type=str, help='输入IP目标或域名：例192.168.3.102:5001 不用加http')
def poc_game3_only(only,target): #单一POC检测
    poc_only = importlib.import_module('pocs.'+only)
    Logger.get_instance().info('当前模式单一POC检测......')
    Logger.get_instance().info('加载POC模块:'+only)
    Logger.get_instance().info('开始检测......')
    try:
        Logger.get_instance().info(poc_only.poc_payload(target)) #传递目标
        
    except:
        Logger.get_instance().error('[-]POC单一检测报错......！')

@main.command()
@click.option('-b', '--batchtest', type=str, help='POC批量检测模式：请输入POC模块名称,目录下的的host.txt为导入IP文件。')
def poc_game3_batchtest(batchtest): #批量POC检测
    ip_target = importlib.import_module('lib.ip_load_target')
    Logger.get_instance().info('当前模式批量POC检测......')
    Logger.get_instance().info('加载POC模块:'+batchtest)
    Logger.get_instance().info('开始检测......')
    try:
        poc_pt = importlib.import_module('pocs.'+batchtest)
        #Logger.get_instance().info(str(ip_target.ip_data(0)+':'+str(ip_target.port_data(0))))
        for i in range(ip_target.ip_munber()):   
            iptarget = ip_target.ip_data(i)+':'+ip_target.port_data(i)
            strecho =str(poc_pt.poc_payload(iptarget))
            Logger.get_instance().info('['+str(i)+']'+strecho)
            File.append(os.getcwd()+'//testdata//'+batchtest+'_'+'.txt', strecho +'  '+str(time.time())+ '\n')
            #Logger.get_instance().info(iptarget)
    except:
        Logger.get_instance().error('[-]POC批量检测报错 不要加.py后缀......！')

@main.command()
@click.option('-zk', '--zmkeyword', type=str, help='zoomeye host输入关键词：,例子 weblogic')
@click.option('-zp', '--zmpage', type=str, help='zoomeye host输入页数：,例子 1-x 页数')
def poc_game3_zoomeyehost(zmkeyword,zmpage):
    zoomeyehost = importlib.import_module('odbcs.zoomeye_host_odbc')
    strtarget =zoomeyehost.zkzy(str(zmkeyword),str(zmpage))
    strdata = int(10) * int(zmpage)
    Logger.get_instance().info('当前加载模块zoomeye host')
    Logger.get_instance().info('开始获取数据......')
    Logger.get_instance().info('关键词：'+str(zmkeyword))
    Logger.get_instance().info('获取页数：'+str(zmpage)) 
    Logger.get_instance().info('获取ip数量：'+str(strdata))
    Logger.get_instance().info('ip写入到目录下的host.txt文本')   
    try:
        for i in range(strdata):
            strecho=strtarget[i]
            Logger.get_instance().info(strecho)
            File.append('host.txt', strecho + '\n')
    except:
        Logger.get_instance().error('[-]zoomeye host模块报错请请检查登录账号是否正确和账号特权......！')
        

if __name__ == '__main__':
    print(FontColor.blue(icobanner))
    main()
 