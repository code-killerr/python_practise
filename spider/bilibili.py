
import requests
import time

def step1():
    url = "https://show.bilibili.com/api/activity/index/anti/prepare"

    payload = {}
    headers = {
        'authority': 'show.bilibili.com',
        'accept': '*/*',
        'access-control-request-method': 'POST',
        'access-control-request-headers': 'content-type',
        'origin': 'https://mall.bilibili.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mall.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    response = requests.request("OPTIONS", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def step2():
    url = "https://show.bilibili.com/api/activity/index/anti/prepare"

    payload = "{\"customerId\":20006,\"assocId\":\"202101263627001\",\"subCustomerId\":2,\"interfaceName\":\"PRIZE_CONVERT\"}"
    headers = {
      'authority': 'show.bilibili.com',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
      'content-type': 'application/json',
      'accept': '*/*',
      'origin': 'https://mall.bilibili.com',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://mall.bilibili.com/',
      'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
      'cookie': 'CURRENT_FNVAL=80; _uuid=96AADD92-2448-46B5-E17A-FB03809CA60247248infoc; blackside_state=1; rpdid=|(u~JY|JYmmk0J\'uY|mkYkm~R; buvid3=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; sid=i9uxudcz; fingerprint=ad0e418c954e3e890eb1d1791026d2d6; buvid_fp=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; buvid_fp_plain=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; DedeUserID=180882922; DedeUserID__ckMd5=ee2afe5c68f13753; SESSDATA=5ac1389a%2C1625744657%2Cff9b9*11; bili_jct=388100667c60ea6d93315bbd0c890f69; PVID=1; Hm_lvt_909b6959dc6f6524ac44f7d42fc290db=1612247762'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

def step3():

    url = "https://api.bilibili.com/open/monitor/report?source=hyg&log=%5B%7B%22level%22%3A%22info%22%2C%22logtype%22%3A1%2C%22url%22%3A%22https%3A%2F%2Fshow.bilibili.com%2Fapi%2Factivity%2Findex%2Fanti%2Fprepare%22%2C%22status%22%3A200%2C%22cost%22%3A142%2C%22traceid_end%22%3Anull%2C%22traceid_svr%22%3A%22%22%2C%22sub_product%22%3A%22warrior%22%7D%5D"

    payload = {}
    headers = {
        'authority': 'api.bilibili.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'image',
        'referer': 'https://mall.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'CURRENT_FNVAL=80; _uuid=96AADD92-2448-46B5-E17A-FB03809CA60247248infoc; blackside_state=1; rpdid=|(u~JY|JYmmk0J\'uY|mkYkm~R; buvid3=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; sid=i9uxudcz; fingerprint=ad0e418c954e3e890eb1d1791026d2d6; buvid_fp=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; buvid_fp_plain=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; DedeUserID=180882922; DedeUserID__ckMd5=ee2afe5c68f13753; SESSDATA=5ac1389a%2C1625744657%2Cff9b9*11; bili_jct=388100667c60ea6d93315bbd0c890f69; PVID=1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def step4(payload):

    url = "https://mall.bilibili.com/mall-dayu/mall-marketing-core/game/exchange_shop/exchange"

    #payload = "xZg0i82Te9hv6dO6M2dwE2ADap62COT5PDg3pGcSch1degCxki5I0WaJkFXOxuFL9BSGj+yJx5Fa5q2A7rNauDYXoXPddnOaC6LKRmXxD1qWxqkg7pBjeSnHwPJ3p/+FV0ro/GSU65QdcuQirGB1t7XvVIi9FzXKfGiKDxnaRMT3dtyWXY/noQ=="
    headers = {
        'authority': 'mall.bilibili.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://mall.bilibili.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mall.bilibili.com/newwarrior/index.html?noTitleBar=1&loadingShow=true',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'CURRENT_FNVAL=80; _uuid=96AADD92-2448-46B5-E17A-FB03809CA60247248infoc; blackside_state=1; rpdid=|(u~JY|JYmmk0J\'uY|mkYkm~R; buvid3=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; sid=i9uxudcz; fingerprint=ad0e418c954e3e890eb1d1791026d2d6; buvid_fp=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; buvid_fp_plain=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; DedeUserID=180882922; DedeUserID__ckMd5=ee2afe5c68f13753; SESSDATA=5ac1389a%2C1625744657%2Cff9b9*11; bili_jct=388100667c60ea6d93315bbd0c890f69; PVID=1; Hm_lvt_8d8d2f308d6e6dffaf586bd024670861=1612247878; bsource=search_baidu'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def step5():

    url = "https://api.bilibili.com/open/monitor/report?source=hyg&log=%5B%7B%22level%22%3A%22info%22%2C%22logtype%22%3A1%2C%22url%22%3A%22https%3A%2F%2Fmall.bilibili.com%2Fmall-dayu%2Fmall-marketing-core%2Fgame%2Fexchange_shop%2Fexchange%22%2C%22status%22%3A200%2C%22cost%22%3A97%2C%22traceid_end%22%3Anull%2C%22traceid_svr%22%3A%22%22%2C%22sub_product%22%3A%22warrior%22%7D%5D"

    payload = {}
    headers = {
        'authority': 'api.bilibili.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'image',
        'referer': 'https://mall.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'CURRENT_FNVAL=80; _uuid=96AADD92-2448-46B5-E17A-FB03809CA60247248infoc; blackside_state=1; rpdid=|(u~JY|JYmmk0J\'uY|mkYkm~R; buvid3=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; sid=i9uxudcz; fingerprint=ad0e418c954e3e890eb1d1791026d2d6; buvid_fp=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; buvid_fp_plain=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; DedeUserID=180882922; DedeUserID__ckMd5=ee2afe5c68f13753; SESSDATA=5ac1389a%2C1625744657%2Cff9b9*11; bili_jct=388100667c60ea6d93315bbd0c890f69; PVID=1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))

def link():
    dt = '2021-02-03 18:00:00'
    ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    payload = [r'xZg0i82Te9hv6dO6M2dwE2ADap62COT5PDg3pGcSch1degCxki5I0WaJkFXOxuFL9BSGj+yJx5Fa5q2A7rNauDYXoXPddnOaC6LKRmXxD1qWxqkg7pBjeSnHwPJ3p/+FV0ro/GSU65QdcuQirGB1t7XvVIi9FzXKfGiKDxnaRMT3dtyWXY/noQ==',
               r'gXYHfEcQMgEY6gPVguzgcXxaBYxlILO3Dt/OIldVGmapABw7pHXJklRtlKf6/DncMrhueFkS/qBk16lK2dIQAye9WMeCTSFv0cND6GfOb+8N05YFaUCP94IC16UnzwkumFaiep9LVeYXwAUNJnR8wQZeHhFVKmCDtNwyBk1VuP5iwVdwaKFObA==',
               r'0BaTQhVPwsV6VY9KLXFxv5qfyaF7wrCvKoxAJgNIAu+mlTB1s4wmWPHhXPkKz0fZzHvsCeVumlWtWIAdqM5XK36KlH8r9P9ho+eTmGjZ5NYm67nimYg5xKBdf7FokEKC8yZQSr33O6H8KienxMQdPcC+bRVWTYjF5aPypC3oh3UCpTLgDwdj9Q==',
               r'a2VZdtCTTQB6Blu4XHKncfPzo+wPkUfFaOjohSwJguO/U2OgUzJphIj+vdG5y+bp5hJkGZPu5k4CjB6Ys6znH3lAHrHKmpKed6UFWWRQS7KqqtjWjHg+jm0O9JJmFaD9yCDZIrc2I+AYu3kztjJWZwtCyxASDFG+DNL53N8ZrF9HlkKkSWzyeQ==',
               r'Suipyh3eDpRMN7l1PDY4XHJ7hevIxNvrHWuY55g1GGf11zl/tB1J8EfRKQDWD1meE98cvJiGyaBGWHL3G67kJKObYCPfyOuQHvBjrApUPOCiBVx+IEuAo4Du5oW+TuozSAZhhiUS9HBiYac6dNVct71o9Az5rP38UJ6N5fXEXAf9fywlIsbGfQ==',
               r'Suipyh3eDpRMN7l1PDY4XHJ7hevIxNvrHWuY55g1GGf11zl/tB1J8EfRKQDWD1meE98cvJiGyaBGWHL3G67kJKObYCPfyOuQHvBjrApUPOCiBVx+IEuAo4Du5oW+TuozSAZhhiUS9HBiYac6dNVct71o9Az5rP38UJ6N5fXEXAf9fywlIsbGfQ=='
               ]
    while True:
        if time.time() > ts:
            step1()
            for goods in payload:
                try:
                    step2()
                    step3()
                    step4(goods)
                    step5()
                except Exception as e:
                    print("error")
                    continue
                time.sleep(0.1)
            break

def getPic(savePath):

    url = "https://show.bilibili.com/openplatform/verify/tool/open/captcha/get"

    payload = 'ct=eyJ0c3RJZCI6IkFXRlErTy9uK3FLRzZzWSsiLCJjdXN0b21lcklkIjoiUVpFVGswQ2Vubzg3dCtBSCIsInRpbWVzdGFtcCI6InFlYzBadVNiWG1qNy9OWWpwdEpXU21ibWRyOD0iLCJkZXZpY2VJZCI6Ilo0UDlWdFNVRXpEY0VNUVFjMFM4TmJQdUhPRUE1Smg5OE5pYzlDeWpSUmc5d0tnSyIsImFwcFR5cGUiOiJkdE96RDhhS1Jrcz0iLCJkZXZpY2VUeXBlIjoiY0NnbEtZanI5OVE9IiwibmV0d29yayI6Iml6VkVXZER2N2ZjPSJ9&business=shield&voucher=Vh6FaIwQPhSnzKCKybRb62n+d21btcDEvv3d2zDEFhXdXTpaEdZND2fQAA2hp1w2geutgjsamAakb2OvibJR4fpv2tRHlPIHo1qjMfLNeH1js29XuGUi4gWC7GxTfAg/sLmV/x05Udqyyjdo5OScPaia935o057vfZhPLmLWFpa0DaLdjn4IOiPth+MBndLlvO6xPkG/tyNXUrseuR7AbJY4g5/AHlVBV9kl1xuHqVk%3D&verifyType=1&apiStartTime=1612350233000&csrf=388100667c60ea6d93315bbd0c890f69'
    headers = {
        'authority': 'show.bilibili.com',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://mall.bilibili.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mall.bilibili.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'CURRENT_FNVAL=80; _uuid=96AADD92-2448-46B5-E17A-FB03809CA60247248infoc; blackside_state=1; rpdid=|(u~JY|JYmmk0J\'uY|mkYkm~R; buvid3=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; sid=i9uxudcz; fingerprint=ad0e418c954e3e890eb1d1791026d2d6; buvid_fp=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; buvid_fp_plain=4208CDD6-983E-4140-A778-C7F030447C96143109infoc; DedeUserID=180882922; DedeUserID__ckMd5=ee2afe5c68f13753; SESSDATA=5ac1389a%2C1625744657%2Cff9b9*11; bili_jct=388100667c60ea6d93315bbd0c890f69; PVID=1; Hm_lvt_909b6959dc6f6524ac44f7d42fc290db=1612247762; bsource=search_baidu'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    imageUrl = response["data"]["bg"]

    imageData = requests.request("get",imageUrl, headers=headers).content
    with open(savePath, 'wb') as f:
        f.write(imageData)

if __name__ == '__main__':
    for i in range(22,150):
        getPic(r'E:\前端\直播笔记\vertifyCheck/'+str(i)+'.jpg')
        print("success" + str(i))
        time.sleep(1)
