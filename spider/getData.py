import requests
from lxml import etree
import json
from queue import Queue
import threading
from bs4 import BeautifulSoup
import time
import re
import os
'''
1.获取页面url的生成规则，通过生成规则获取导航页列表
2.通过导航页获取页面url,该url出队列，每个线程负责一个页面的url
3.单个线程按页面url进行数据爬取，放入相应存储空间
4.线程完成事务后整合数据放入总存储空间
5.统计完成事务数，进行数据输出
公共数据:读取url的页面列表，错误页面数,存储文件序号
局部数据:页面数，页面爬取内容，句子数量。
存储数据:页面爬取数据，
线程本身页面数加入总页面数中
        

线程进行url页面循环，通过锁更改全局变量，更改频率与输出频率一致即可
'''
lock = threading.Lock()
#防止由于不检测SSL造成的警告信息
requests.packages.urllib3.disable_warnings()
#反爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36','Connection': 'close'
}
#断线重连次数
requests.adapters.DEFAULT_RETRIES = 3

saveNum = 0     #存储文件开始序号设置

printNum = 20    #打印间隔设置

outputNum = 400   #输出间隔设置

saveFolder = "C:\\getNews\\result-阿拉伯语\\result\\"   #存储路径设置

url = r'https://www.alarabiya.net/ar/latest-news/mainArea/0/mainContent/00/pArea75/0?&pageNo='    #爬取网页网址设置

threadNum = 10 #开启线程数

errorNum = 0   #错误网页数量
totlePageNum = 0    #爬取网页数量
totleSentenceNum = 0    #爬取句子数量
urlPageQueue = Queue() #存储页面url的队列
controlQueue = Queue()#存储意外停止信号
errorIndexNum = 0#目录错误数

def requestData(url,datas = None):
    global errorNum
    flag = False
    for i in range(0,3):
            try:
                if datas == None:
                    response = requests.get(url = url,headers=headers,verify=False,timeout = 60)
                else:
                    response = requests.post(url = url,headers=headers,data = datas,verify=False,timeout = 60)
                flag = True
                break
            except Exception as e:
                print(url+' is error!\n'+str(e)+'\n\n')
                flag = False
                time.sleep(10)
                continue
    if not flag:
        print(url + ' cant connect!!')
        errorNum+=1
        return None
    return response






def getUrl():
    global url
    global urlPageQueue
    global controlQueue
    global errorIndexNum
    urlList = []
    errorPageData = ''
    #1188
    for i in range(1,1189):
        urlList.append(url+str(i))
    for index in urlList:
        while urlPageQueue.qsize()>600:
            time.sleep(50)
        #获取相关页面
        response = requestData(index)
        #检测是否成功
        if response!=None:
            soup = BeautifulSoup(response.text, "html.parser")
        else:
            errorPageData += index+'\n'
            errorIndexNum += 1
            continue
        #整理获得的数据
        src = soup.findAll('li')
        #填充数据
        countBoxError = 0
        for box in src:
            box = box.find('a')
            if box != None:
                urlPageQueue.put("https://www.alarabiya.net"+box['href'])
            else:
                print('no Url '+str(index)+' '+str(countBoxError))
                countBoxError += 1
        print(index+' is done')
        time.sleep(1)
        
    errorPageData += 'errorNum = '+str(errorIndexNum)
    print('urlqueue dead!!!!')
    with open(saveFolder+r"urlLog.txt","w+",encoding="utf-8") as f:
        f.write(errorPageData)
    controlQueue = Queue()



def getData(name):
    print(name+' is start\n')
    #公有变量
    global outputNum
    global printNum
    global saveNum
    global url #存储路径设置
    global saveFolder #爬取网页网址设置
    global errorNum #错误网页数量
    global totlePageNum    #爬取网页数量
    global totleSentenceNum    #爬取句子数量
    #局部变量
    pageNum = 0    #爬取网页数量
    sentenceNum = 0    #句子数量
    data = ''	#数据存储变量
    #检测生成网址的线程是否挂了，挂了后将不会放置缓冲
    
    while True:    
        if not controlQueue.empty():
        #放置缓冲
            if urlPageQueue.qsize() < 20:
                print(name+'is sleep!')
                time.sleep(10)
                continue
        if urlPageQueue.empty():
            break
        #获取当前页面url
        try:
            pageUrl = urlPageQueue.get()
        except Queue.Empty:
            break
        
        #读取当前url中的链接
        response = requestData(pageUrl)
        if response != None:
        #整合页面获取文章url
            if response.status_code != 200:
                print(pageUrl+' statue_code error')
                continue
            soup = BeautifulSoup(response.text, "html.parser")
        else:
            continue
        site = pageUrl
        #页面内容获取规则制定
        body =soup.find(name="div", attrs={"id" :"body-text"})
        if body != None:
            text = body.findAll(name = "p",attrs={"dir":False})
        else:
                print('body is None!!!! in '+site)
                continue
        for content in text:
            #数据预处理
            content = content.text.strip()
            content = content.replace("\n"," ")
            check = content.split(' ')
            if check.__len__() > 9:
            #爬取原始数据进行存储
                sentenceNum += 1
                data+= content+'\n\n'
        #统计爬取页面数量
        pageNum += 1
        #data+= '---------------------------------------------------\n'+site +'\n---------------------------------------------------\n\n'
        if pageNum%printNum == 0:
            print(site+' '+str(sentenceNum)+' '+str(pageNum)+' '+'  '+'by '+name)
        time.sleep(1)
        #录入数据
        
        if pageNum%outputNum == 0:
            #录入爬取数据
            
            data +='\ntotle:'+str(sentenceNum)
            #加锁
            lock.acquire()
            with open(saveFolder+'result'+str(saveNum)+".txt","w+",encoding="utf-8") as f:
                f.write(data)
            saveNum += 1
            #解锁
            lock.release()
            totlePageNum += pageNum
            totleSentenceNum += sentenceNum
            pageNum = 0
            sentenceNum = 0
            data = ''
            print('sentenceNum:'+str(totleSentenceNum)+'\npageNum: '+str(totlePageNum))
            print('errorUrl count :'+str(errorNum))
            print("The web is in:"+pageUrl+'\n')
            #录入统计数据
            dic = {'pageUrl':pageUrl,'errorWebNum':errorNum,'sentenceNum':totleSentenceNum,'pageNum':totlePageNum,'saveNum':saveNum}
            with open(saveFolder+r"count.json","w",encoding="utf-8") as f:
                json.dump(dic,f)
                
    #录入爬取数据
    
    data +='\ntotle:'+str(sentenceNum)
    lock.acquire()
    with open(saveFolder+'result'+str(saveNum)+".txt","w+",encoding="utf-8") as f:
        f.write(data)
        saveNum += 1
    lock.release()
    #录入统计数据
    totlePageNum += pageNum
    totleSentenceNum += sentenceNum
    dic = {'pageUrl':pageUrl,'errorWebNum':errorNum,'sentenceNum':totleSentenceNum,'pageNum':totlePageNum,'saveNum':saveNum}
    with open(saveFolder+r"count.json","w",encoding="utf-8") as f:
        json.dump(dic,f)
    print(name+' is out')
    
    
    
if __name__ == '__main__':
    if os.path.exists(saveFolder+r"count.json"):
        with open(saveFolder+r"count.json","r",encoding="utf-8") as f:
            data = json.load(f)
        errorNum = int(data['errorWebNum'])
        totlePageNum = int(data['pageNum'])
        saveNum = int(data['saveNum'])
        totleSentenceNum = int(data['sentenceNum'])
    else:
        dic = {'pageUrl':0,'errorWebNum':0,'sentenceNum':0,'pageNum':0,'saveNum':0}
        with open(r"count.json","w+",encoding="utf-8") as f:
            json.dump(dic,f)
        errorNum = 0
        totlePageNum = 0
        saveNum = 0
        totleSentenceNum = 0
        
    for i in range(1,5):
        controlQueue.put(i)
    threadList = []
    
    #测试
    #urlPageQueue.put('https://news.un.org/sw/story/2020/03/1084592')
    #getUrl()
    #getData('1号')
    #创建线程
    #启动获取url线程
    getUrlThread = threading.Thread(target = getUrl)
    getUrlThread.start()
    #等待queue填充
    time.sleep(20)
    for i in range(0,threadNum):
        threadList.append(threading.Thread(target = getData,args = (str(i)+'号',)))
    for thread in threadList:
        thread.start()
        time.sleep(1)
    #监控线程
    
    flag = True
    logData = ''
    while flag:
        time.sleep(600)
        flag = False
        for i in range(0,threadNum):
            if threadList[i].isAlive():
                logData += str(i)+'号正在运行\n'
                flag = True
            else:
                logData += str(i)+'号停止运行\n'
        if getUrlThread.isAlive():
            logData += 'url获取线程正在运行'
        else:
            logData += 'url获取线程挂了'
        with open(saveFolder+r"log.txt","w+",encoding="utf-8") as f:
            f.write(logData)
        logData = ''
    




        