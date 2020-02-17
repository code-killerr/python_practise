#此时为一个模块，放在调用程序的文件夹下即可调用，Py文件名为模块名，可以Import导入模块调用其中函数
def hello():
    #外层调用该函数使用文件名.hello()即可
    print('helo world')
#from 模块名 import 函数名可以直接导入函数，再加as可以重命名
#模块测试    
def test():
    print(hello())
import urllib
def translation():
    url = r'https://fanyi.baidu.com/'
    data = {}
    data['aldtype']=r'16047#en/zh/hello%20world!'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.urlopen(url,data)
    txt = req.read().decode('utf-8')
    print(txt+' '+str(req.getcode()))
    
if __name__ == '__main__':
    translation()