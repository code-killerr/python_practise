#o p e n ( f i l e , m o d e = 'r', b u f f e r i n g = -  1, e n c o d i n g = N o n e )第一个参数为文件路径，第二个为打开模式，默认为r
''' r 以只读方式打开文件
w 以写入的方式打开文件，会覆盖已存在文件
x 如果文件存在，此模式打开会引发异常
a 以写入模式打开，如果文件存在，则在末尾追加写入
b 以二进制模式打开文件
t 以文本模式打开
+ 可读写模式
U 通用换行符支持'''
f=open('1.txt')
print(f)
print(f.read())#读取文件内容，f.read(size=-1)从文件读取size个字符，未给定size或size负值时，读取剩余所有字符，并作为字符串返回
print(f.read())#文件指针指向末尾，无法继续读取，所以为空
print(f.tell())#表示文件指针位置在第几个数据处
f.seek(0,0)#f.seek(offset,from)在文件中移动文件指针，从from偏移offset个字节，from中0代表起始位置，1代表当前位置，2代表文件末尾,只有一个参数时参数设置为from
print(f.read(3))
print(f.readline())#读取一行
#f.write("11111")#报错，因为打开方式为只读，无法写入
f.close()#关闭文件，使用完后关闭完成数据录入
f = open('2.txt','w')
f.write('你好啊')#文件写入
f.close()
