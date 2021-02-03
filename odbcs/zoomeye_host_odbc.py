#! /usr/bin/python3
#钟馗之眼
#author by Greekn 

import zoomeye,configparser,requests,sys,json,os

def zkzy(keyword,page):   
    conf = configparser.ConfigParser()
    conf.read(os.getcwd()+"\\odbcs\\config.ini")      
    ID = conf.get("zoomeye","ID")
    password = conf.get("zoomeye","password")
    zm = zoomeye.ZoomEye()
    zm.username = ID
    zm.password = password
    print('zoomeye登录成功:'+zm.login())
    apstr = keyword  #输入关键词
    pages = int(page)+int(1) #页数
    apiurl = "https://api.zoomeye.org/host/search?query="+apstr+"&page="
    headers ={'Authorization':'JWT'+' '+zm.login()}
    results = []
    for mun in range(1,int(pages)):       
        #print('number:'+str(mun))
        openurl = requests.get(apiurl+str(mun),headers=headers)
        data = json.loads(openurl.text)
        for s in data['matches']:
            ipstr = str(s['ip'])+':'+str(s['portinfo']['port'])
            results.append(ipstr)

    return results
    

