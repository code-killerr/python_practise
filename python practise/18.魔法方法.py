#魔法方法用双下横线包围
#__init__(self[....])相当于构造函数，构造函数不能有返回值
class A:
    def __init__(self):
        return 111;
#a = A()#报错，构造函数应返回none
#__new__(cls[....])在init之前调用的方法，传入参数为类，返回值为对象
class B(str):
    def __new__(cls,string):
        string = string.upper()#执行将字符串大写的操作
        return str.__new__(cls,string)#返回str的__new__魔法方法返回的实例
a = B("hello python")#由于当前重写构造函数会造成str的构造方法被覆盖，得不到相应的效果，所以重写当前类的new方法来实现效果后调用str的new方法生成对象，应该这样理解吧
print(a)
#__del__析构方法，类结束后调用
class C():
    def __del__(self):
        print('调用del方法')
c1 = C()
c2=c1
del c1#此处并没有调用del方法
print('\n,分割一下')
del c2#析构方法调用的条件是没有指向它的东西
    
