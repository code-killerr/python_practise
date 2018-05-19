class Pyclass(list):#python中类名约定以大写字母开头,括号中为继承的类
    color1 = 'red'
    name = 'python'
    
    def printf(self):#声明方法
        print(self.name)#在方法中传入类的参数需要使用self调用，所以在方法中需要传入self
    def color(self):
        print("the color is %s" % self.color1)#测试发现python类疑似中默认有color等方法，变量名和那个一样会出现诡异的对象
P1 = Pyclass()#生成对象
P1.printf()
P1.color()
P1.append(3)#执行继承类list中的方法
P1.append(4)
print(P1)
#OOA面向对象分析 OOD面向对象设计 OOP面向对象编程
#方法中self相当于this
class Ball:
    __password = 00000#使用两个下划线表示隐藏变量，然而外部仍可使用_类名__变量名调用
    def __init__(self):#构造函数，生成对象时默认调用
        self.name = "nobody"
        self.__password = 123456
    def setName(self,name):
        self.name = name#python可以在方法内定义类的成员
    def Introduction(self):
        print("I am %s" % self.name)
        print("my password is:%d" % self.__password)
a = Ball()
b = Ball()
c = Ball()#调用构造函数
a.setName('小A')
b.setName('小B')#调用方法
a.Introduction()
b.Introduction()
c.Introduction()#name出现默认设置的值
print(a.name)#python中类中成员默认公有
#print(a.__password)#类外部调用隐藏变量报错
print(a._Ball__password)#然而伪私有仍然可以被外部调用，这就有点坑了
class Parent:
    def hello(self):
        print('这里是parent')
class Parent2:
    def hello(self):
        print('这里是parent2')
class Parent3(Parent2):
    def hello(self):
        print('这里是parent3')
class Child(Parent):
    pass#类中不使用任何方法
p = Child()
p.hello()
print('\n')
class Child1(Parent):
    def hello(self):
        print('这是Child')
P = Child1()
P.hello()#如果子类中具有相同名称方法将覆盖父类中的方法，当然如果用父类定义对象使用的是父类方法
a = Parent()
a.hello()
print('\n')
class Child2(Parent3):#多重继承
    def hello(self):
        Parent.hello(self)#使用未绑定的父类方法来执行覆写的内容
        super().hello()#可以使用super方法可以不需要使用父类的名字执行覆写内容
        #研究表明super只会执行父类中的相关方法，无法执行父类的父类中相关方法
        #在有多个父类方法相同时，优先使用第一个父类的方法
        #https://rhettinger.wordpress.com/2011/05/26/super-considered-super/有super详细用途
        print('这是Child')
b = Child2()
b.hello()
print('\n')
#此方法相当于执行
Parent2.hello(b)

