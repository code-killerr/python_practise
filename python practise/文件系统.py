import random#随机数模块
ser = random.randint(1,10)#使用模块中函数生成随机数
print(ser)#模块为包含其定义的函数和变量的文件，后缀为.py可被引入
import os#os模块，可以实现从各种系统中读取文件等各种功能
print(os.getcwd())#返回当前工作目录
os.chdir('E:/python')#更改工作目录
print(os.getcwd())
print(os.listdir('E:/python'))#列举指定目录中的文件名
os.mkdir('E:A')#创建单层目录，如果存在抛出异常
os.mkdir('E:A/B')#可以在当前工作目录已有的目录中创建子目录.如若没有父目录报错
os.makedirs('E:/B/C')#递归创建多层目录,也可以用来创建单层目录
os.makedirs('E:/B/D')
#在路径的盘符后如果不加反斜杠且盘符为工作目录所在的盘符将会在工作目录下创建文件夹
#如果带有反斜杠则为在标定目录下创建文件夹
open('E:A/B/1.txt','w')
os.remove('E:A/B/1.txt')#删除文件
os.rmdir('E:A/B')#删除单层目录，只能删除空目录
os.rmdir('E:A')
os.removedirs('E:/B/C')#递归删除目录，目录必须为空,其中的路径为目录中最深的目录
#使用removedirs注意其判定条件为从最深的目录开始删，遇到非空目录时终止删除
#例如在B目录中存在C和D两个目录，使用removedirs('E:/B/C')会先删除C目录然后判断B目录是否为空
#不为空则终止，然而此时B目录中存在D目录，故删除停止，只会删除C目录
os.removedirs('E:/B/D')
