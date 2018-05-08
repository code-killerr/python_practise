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
open('1.txt','w')
os.rename('1.txt','2.txt')#将文件old重命名为new
os.system('calc')#运行系统shell命令，calc为计算器，cmd为docs
print(os.listdir(os.curdir))#当前目录,pardir上一个目录
print(os.name)#当前操作系统('posix','nt','mac','os2','ce','java')第一个为linux第二个为windows
from os import path#path模块中的函数
print(path.basename('E:/a/b/33.mp4'))#去掉路径返回文件名
print(path.dirname('E:/a/b/33.mp4'))#去掉文件名返回路径
print(path.join('E:\\','a','b','33.mp4'))#将各部分组合成路径名
print(path.split('E://a//b//33.mp4'))#返回一个元组具有路径和文件名两个元素，如果只有路径第二个元素为末尾文件名
print(path.splitext('E://a//b//33.mp4'))#返回文件名和扩展名
print(path.getsize('3.txt'))#返回文件大小，字节为单位
import time
print(time.gmtime(path.getatime('3.txt')))#返回文件最近访问时间，单位为秒,可以使用time模块中gmtime或localtime转换
#getctime 返回指定文件创建时间，getmtime 返回指定文件最新修改时间
#isabs() 判断指定路径是否为绝对路径
#exists() 判断路径/目录/文件是否存在
#isdir() 判断路径是否存在且为一个目录
#isfile() 判断路径是否存在且是一个文件
#islink() 判断指定路径是否存在且是一个符号链接(例如快捷方式)
#ismount() 判断是否存在且为为挂载点(例如C盘，D盘)
#samefile(path1,path2)#判断path1和path2两个路径是否指向相同文件