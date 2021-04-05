# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:14:52 2019

@author: Administrator
"""
#图文类型为news
from urllib import request
accessToken = ""
mediaType = "news"
offset=0
count=1
postUrl = ("https://api.weixin.qq.com/cgi-bin/material" "/batchget_material?access_token=%s" % accessToken)
postData = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }" % (mediaType, offset, count))
postData = postData.encode("utf-8")
urlResp = request.urlopen(postUrl,postData)
print(urlResp.read())
