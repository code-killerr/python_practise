# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:43:30 2019

@author: Administrator
"""

from urllib import request
accessToken = "22_Klz6ySu8Fxir1bATWQdmMMhS_JmtJu5PWo001G8qesflPAPGO3uV0O2IrAV_I4FAzriETJIFMSXZi-SpGNQ1iAofgi24-R9GWgEOy3fTnMi_4EZFTkzgl3db_52FUkI46gMpDvCRvGobhPw1YYZfADAMMN"
mediaType = "news"
offset=0
count=1
media_id = "U76KCcola8c5GSBTTc8CtxX7MiyJgnURe5eXO1HlTxc"
postUrl = ("https://api.weixin.qq.com/cgi-bin/material/get_material?access_token=%s" % accessToken)
postData = ("{\"media_id\":\"%s\"}" % media_id)
postData = postData.encode("utf-8")
urlResp = request.urlopen(postUrl,postData)
print(urlResp.read())