# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:21:56 2019

@author: Administrator
"""

import werobot
import random
import requests
from werobot.replies import ImageReply
robot = werobot.WeRoBot(token = "23333")
robot.config["APP_ID"] = "wx8bf6453edd855942"
robot.config["APP_SECRET"] = "5f99c5a02e77602bc216b904ee6aee4f"

@robot.subscribe
def subscribe(message):
    return "欢迎关注我呀"


client = robot.client
#获取acceaccess token
acceaccess_token = client.get_access_token()
url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + str(acceaccess_token)
#自定义菜单目录
'''
menu = {
    "button":[
    {
        "type": "scancode_waitmsg",  
        "name": "sao"  
    }]
}
    '''
    
menu =  {
 "button": [
        {
            "name": "扫码", 
            "type": "scancode_waitmsg", 
            "key": "qcore", 
        }]
}
 


  
    
#创建自定义菜单
bacg = client.create_menu(menu_data=menu)
#提交数据
@robot.handler
def music(message):
    return message.scan_result
response = requests.post(url,bacg)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()