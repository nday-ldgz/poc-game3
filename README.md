# poc-game3

![image](https://img.shields.io/badge/poc--game3-python3.x-blue) ![image](https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.0.0-brightgreen) ![image](https://img.shields.io/badge/poc%E6%95%B0%E9%87%8F-1-yellowgreen) ![image](https://img.shields.io/badge/star-1-yellow)

poc-game3 一款批量漏洞扫描验证工具 

编程语言：python3

版本：V1.0.0



## 目录结构：

   	banner_scan banner 扫描库 待更新

	  basic 基础库  待更新

	  odbc 数据源库

	  pocs 漏洞库

	  verify 验证库 待更新
	
	  requirement.txt python库 

	  lib 核心代码库



## 部署流程：

	github clone https://github.com/nday-ldgz/poc-game3.git
	
	pip3 install -r requirement.txt 





## 运行命令：
C:\Users\Administrator\Desktop\poc-game3>poc_game3_main.py --help

	 _____   _____   _____        _____       ___       ___  ___   _____   _____
	|  _  \ /  _  \ /  ___|      /  ___|     /   |     /   |/   | | ____| |___  |
	| |_| | | | | | | |          | |        / /| |    / /|   /| | | |__      _| |
	|  ___/ | | | | | |          | |  _    / / | |   / / |__/ | | |  __|    |_  {
	| |     | |_| | | |___       | |_| |  / /  | |  / /       | | | |___   ___| |
	|_|     \_____/ \_____|      \_____/ /_/   |_| /_/        |_| |_____| |_____/

	poc-game3 一款批量漏洞扫描验证工具

	当前版本：V1.0.0
	
	测试命令用法实例:

	poc_game3_main.py poc-game3-pocs -p pocs_list 列出漏洞模块

	poc_game3_main.py poc-game3-pocinfo -v CVE-2020-3019_lanproxy_dta 加载漏洞模块查看漏洞信息

	poc_game3_main.py poc-game3-zoomeyehost -zk lanproxy -zp 2 获取目标关键词ip

	poc_game3_main.py poc-game3-ipnumber -n  ip_load_target 查看ip 数量

	poc_game3_main.py poc-game3-batchtest -b CVE-2020-3019_lanproxy_dta 加载漏洞模块批量漏洞测试 不要加.py 后缀

	poc_game3_main.py poc-game3-only -o CVE-2020-3019_lanproxy_dta -t 127.0.0.1:8080 加载漏洞模块单一漏洞测试 不要加.py 后缀

	Usage: poc_game3_main.py [OPTIONS] COMMAND [ARGS]...

	Options:
	  --help  Show this message and exit.

	Commands:
	  poc-game3-batchtest 批量漏洞检测模块
	  poc-game3-ipnumber 查看ip数量模块
	  poc-game3-only 单一漏洞检测模块
	  poc-game3-pocinfo 查看漏洞模块信息
	  poc-game3-pocs 列出POCs仓库里面的模块
	  poc-game3-zoomeyehost zoomeye获取ip数据源模块

