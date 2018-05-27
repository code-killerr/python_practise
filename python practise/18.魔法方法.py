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
a = B("hello python")
print(a)
    
