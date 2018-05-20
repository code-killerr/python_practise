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
class LittleA:
    def __init__(self,x):
        self.num = x
class LittleB:
    def __init__(self,x):
        self.num = x
class BigAB:
    def __init__(self,x1,x2):#在其它类中可以调用别的类
        self.A = LittleA(x1)
        self.B = LittleB(x2)
    def printf(self):
        print("bigAB有 %d个小A和%d个小B" % (self.A.num,self.B.num))
P = BigAB(5,6)
P.printf()
#python中先定义类，定义完成后生成类对象，再由类对象创建实例对象，一个类所有的对象对应一个类对象，由实例对象执行各种方法
#根据python的特性，相同值的变量属于同一ID，所以如果在类中定义变量，注意不是方法中
#改变该变量的值，将会改变所有对象中该变量的值，除非在方法中或者自行覆写了该变量
#这时候相当于改变了变量的ID，给变量一个新的内存，所以不会受到影响，在python中，生成实例对象后其中方法和变量都可以自行覆写
#甚至可以将对象中的方法覆写成变量，比如可以将关键字方法覆写成变量酱紫的，就是这个特性
class CC:
    count = 0
    def Change(self):
        self.count = 20
a = CC()
b = CC()
c = CC()
print(a.count,b.count,c.count)
a.Change()#此处a调用了Change方法覆写了count，所以不受到CC.count改变的影响,相当于做了类对象的拷贝
CC.count = 100#改变了类对象的值，类对象的值无法通过实例对象改变，实例对象的值改变只是将其相应的变量覆写，扔到另一个内存中
print(a.count)
print(b.count)#其余只是算作将count变量换了个名称而已，所以仍受到CC.count的影响，并不算是拷贝
print(c.count)
print(CC.count)
a.Change=33
print(a.Change)
#a.Change()#此时覆写了a中的Change方法，这玩意变成了变量，不可再使用方法形式调用，报错
#注意类中的方法调用方式和人还不一样，xx.AAA()中，定义AA方法时有一个self，而XX.AA()相当于AA(xx)但类中仍然需要有相关方法
class AA:
    def __init__(self):
        self.count = 0
    def aa(self):
        self.count = 10
        print(self.count)
    def bb(self):
        self.count +=10
        print(self.count)
    def printf():
        print('what the fuck!!!!')
#AA.aa()#报错，因为需要实例化对象来提供self参数
AA().aa()#可以直接自己实例化自己调用相关方法，如果有构造函数还可以实例自己的同时调用自己的构造函数，卧槽啥玩意
AA().bb()#如果没有构造函数报错，有构造函数会自动调用构造函数，将实例化的自己塞进self里，这个属于类对象，即类的实例化
#当然，如果构造函数里没有方法里的变量仍会报错，应该可以证明自己可以实例自己，但是并不会储存相关变量，只是单纯的调用方法而已
print('\n')
dd = AA()
dd.aa()
dd.bb()#可以对比一下，可以用自己实例化自己来强行调用一些没有外来变量的方法
print('\n')
AA.printf()#由于该方法不需要self可以自身调用方法，如果加了self并且函数没有外来变量可以替换成使用类自己实例化自己来调用
print(AA().__dict__)#这里可以显示自己实例化了自己并调用了构造函数，虽然并不存在相关方法，但是删除类后仍可调用相关方法
#因为类中方法是静态的，哪怕删除了类,仍然保存在内存中可以调用
print(AA.__dict__)#这里显示了类中的所有属性
#理解类对象和实例对象还需要多加练习才能搞明白