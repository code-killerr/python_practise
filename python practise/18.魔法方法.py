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
print('----------------------------------------------')
del c2#析构方法调用的条件是没有指向它的东西
#__add__(self,other)定义加法运算+__sub__定义减法运算
class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)#调用int类中的sub方法执行减操作
    def __sub__(self,other):
        return int.__add__(self,other)#调用int类中的add方法执行+操作
a = New_int(7)
b = New_int(10)
print(a+b)#由于错位所以使用+方法实际执行减操作
print(a-b)
class D(int):
    def __add__(self,other):
        return int(self)+int(other)#注意返回类型
a = D(12)
b = D(11)
print(a+b)
#其它魔法方法
'''
__mul__(self,other)定义乘法：*
__truediv__(self,other)定义真除法:/
__floordiv__定义整数除法://
__mod__定义取模:%
__pow__(self,other[:modulo])定义幂运算时操作
__divmod__(a,b)把除数和余数的运算结果返回，返回的为(a//b,a%b)酱紫的元组
pyhthon中魔法方法都可以自己改写
'''
'''
class int(int):
   def __add__(self,other):
        return int.__sub__(self,other)
print(int(5)+int(3))#酱紫乱改的
'''
#若a+b 时由a调用__add__方法，但如果__add__a没有__add__方法会让b来调用__radd__方法
class E(int):
    def __radd__(self,other):
        return int.__sub__(self,other)
a = E(10)
b = E(7)
print(a + b)#a拥有__add__方法调用正常的__add__方法
print(5+b)#5没有__add__方法调用b的不正常的__radd__方法
class F(int):
    def __rsub__(self,other):
        return int.__sub__(self,other)#看起来放的是正常的__sub__方法
a = F(5)
print(6-a)#然而答案不正常
#根据传参，由于是a调用的__rsub__方法，所以self传入a,other自然是6，所以答案会为a-6在写rsub应传参为(other,sub)
#增量赋值运算，例如+=,-=之类的仍然可以改写,对应方法前加i即可，+=魔法方法为__iadd__
#一元操作符，__neg__(self)+x,__pos__(self)-x,__abs__(self)~x
class G():
    def __str__(self):#str魔法方法表示直接打印对象时返回的东西
        return "123456"
    def __repr__(self):#直接调用该类对象时返回
        return"654321"
g = G()
print(g)
#命令行中输入g会返回654321