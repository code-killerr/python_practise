# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:43:30 2019

@author: Administrator
"""

from urllib import request
accessToken = ""
mediaType = "news"
offset=0
count=1
media_id = ""
postUrl = ("https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken)
postData = ("{\"media_id\":\"%s\"}" % media_id)
postData = postData.encode("utf-8")
urlResp = request.urlopen(postUrl,postData)
print(urlResp.read())