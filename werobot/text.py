# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:31:45 2019

@author: Administrator
"""

import werobot
from werobot.replies import VoiceReply
from werobot.replies import ImageReply
from werobot.replies import ArticlesReply
import re
import random
robot = werobot.WeRoBot(token='23333')
#没有权限无法使用菜单
robot.config["APP_ID"] = "wx1b511332da51705d"
robot.config["APP_SECRET"] = "6b59ee02b4d1e5776f5ba5abe249b2a9"

client = robot.client

#client.create_menu({
#    "button":[{
#         "type": "click",
#         "name": "今日歌曲",
#         "key": "music"
#    }]
#})

#@robot.key_click("music")
#def music(message):
#    return '你点击了“今日歌曲”按钮'
###
#robot.config["APP_ID"]="wx1b511332da51705d"
#robot.config["APP_SECRET"]="6b59ee02b4d1e5776f5ba5abe249b2a9"
#上传文件获取media_id,该id只能在media list中或者上传时获取
#media_id = client.upload_permanent_media("voice",open(r"hsxw.mp3","rb"))
#print(media_id)
img_id = "U76KCcola8c5GSBTTc8Ct37FEVC_uVZr2RycBHMwhvY"
voice_id = "U76KCcola8c5GSBTTc8Ct6anHwNxOCiZ06xgf3ld0Vw"
news_id = "U76KCcola8c5GSBTTc8CtxX7MiyJgnURe5eXO1HlTxc"
say=["恩恩(假装很懂的样子(￣.￣))","这是一个问题","这个问题好深奥啊","还是看你吧"]
do=["我在想你啊(*/ω＼*)","你猜猜看啊(｀・ω・´)","我也不知道在干嘛(´▽`)ﾉ ","我在看着你哦((〃'▽'〃)ding~~)"]
@robot.subscribe
def subscribe(message):
    return "哇！！！又是一个小伙伴哦，\n我是小菜鸡，欢迎和我聊天哦(兴奋脸！！！)"

@robot.handler
def echo(message):
    # 提取消息
    msg = message.content
    # 解析消息
    if  re.compile(".*?你好.*?").match(msg) or\
        re.compile(".*?嗨.*?").match(msg) or\
        re.compile(".*?哈喽.*?").match(msg) or\
        re.compile(".*?hello.*?").match(msg) or\
        re.compile(".*?hi.*?").match(msg) or\
        re.compile(".*?who are you.*?").match(msg) or\
        re.compile(".*?你是谁.*?").match(msg) or\
        re.compile(".*?你的名字.*?").match(msg) or\
        re.compile(".*?你谁啊.*?").match(msg) or\
        re.compile(".*?什么名字.*?").match(msg) :
        return "你好~\n我是菜鸡家萌萌哒φ(>ω<*) 的机器人哦，他是大菜鸡，我就是小菜鸡辣ヾ(=･ω･=)o（绅士脸）"
    elif re.compile(".*?(厉害|棒).*?").match(msg):
        return '承让承让 (๑•̀ㅂ•́)ﻭ✧'
    elif re.compile(".*?想你.*?").match(msg):
        return '我也想你'
    elif re.compile(".*?miss you.*?").match(msg):
        return 'I miss you,too'
    elif re.compile(".*?我爱你.*?").match(msg):
        return '我也爱你'
    elif re.compile(".*?love you.*?").match(msg):
        return 'I love you,too'
    elif re.compile(".*?美女.*?").match(msg):
        return '我是男生哦♂'
    elif re.compile(".*?帅哥.*?").match(msg):
        return '谢谢夸奖 (๑•̀ㅂ•́)ﻭ✧'
    elif re.compile(".*?是傻逼.*?").match(msg):
        return '我觉得你也是啊'
    elif re.compile(".*?傻逼.*?").match(msg):
        return '爸爸不想理你'
    
    elif re.compile(".*?(干啥|干什么|在干嘛).*?").match(msg):
        return do[random.randint(0,3)]
    elif re.compile(".*?图片.*?").match(msg):
        reply = ImageReply(message = message,media_id = img_id)
        return reply
    elif re.compile(".*?唱.*?歌.*?").match(msg):
        reply=VoiceReply(message = message,media_id = voice_id)
        return reply;
    elif re.compile(".*?音乐.*?").match(msg):
        reply=VoiceReply(message = message,media_id = voice_id)
        return reply;
    elif re.compile(".*?(吗|呢).*?").match(msg):
        return say[random.randint(0,3)]
    elif(msg == '文章'):
        #reply = client.send_news_message(message.source,news_id)#只有认证才可以进行客服消息回复，不然只能调取外部数据，使用Reply不接受media_id
        #return reply
        return "不好意思啊，我还没进行认证，无法发送微信文章哦"
    else:
        return msg




robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()