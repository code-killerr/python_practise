#注意顶行输入，否则报错
print("hello world")#输入
print(5+3)#print后没f
#printf(5*3) 报错
5+3#IDLE可执行，文件中可存在报错
print(2131234123124123124214*12312312441212412413123)#python 类型无位数限制
print("hello"+" "+"world")#可执行字符串链接功能
print("hello\n"*5)#可进行字符串重复
print("second", "example")
a=input()#input是一个bif(Built-in functions)，需要后期转换类型,类型默认str
print(a)
print(type(a))
if(int(a)!=3):#if else 后跟冒号，使用缩进来判断是否循环内
    print("can not change type from str to int")
else:
    a=int(a)#不转换默认str类型转换如果遇到非int型数据报错  
    print(a)
    print(type(a))
#dir(__builtins__)#python 提供的bif及其他注意下划线是两个,在IDLE输入框中输入
#help(xxx)#bif及其他的用法介绍
    
    

