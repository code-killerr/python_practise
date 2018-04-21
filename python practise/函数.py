def Function():#使用def创建函数
    print('hello function')
Function()
def FirstFunction(name):#函数的参数添加
    print(name+' function')
FirstFunction('hello')
def Add(num1,num2):#多个参数的函数
    print(num1+num2)
Add(3,6)
def Add(num1,num2):
    '做两个参数的加操作，num1和num2为形参'#函数文档
    return num1+num2#返回数值
print(Add(4,6))
print(Add.__doc__)#展示函数属性文档，双下横线
print(help(Add))#展示函数，使用help包含格式，使用__doc__无格式
def Function(say,word):
    print(say+' '+word)
Function(say='hello',word='funtion')#关键字参数，使函数的形参直接等于要赋予的参数，防止顺序错误导致参数传入错误
def Function(say='hello',word='world'):#默认参数，当函数形参没有赋值时将默认参数给予形参
    print(say+'->'+word)
Function()
def test(*a):#参数前加上*号代表可变参数/收集参数，输入参数列入元组中
    print('参数长度为:',len(a))
    print('二号参数为',a[1])
test('hello','world',231)
def test(*a,word):#收集参数与关键字参数混合
    print('参数长度为',len(a))
    print('参数word为',word)
test(1,2,3,'we',word='hello')#如果关键字参数没有默认值，不使用关键字赋值会报错，所有参数被归纳到元组中，后面参数没有数值
#函数具有返回值，没有返回值的可以称为过程，python只有函数没有过程
def hello():
    print("hello world");
temp = hello()#函数将返回空
print(temp,type(temp))#函数没有返回值返回空，有返回值返回，所以python没有过程
def back():
    return[1,2,3,"hello world"]#python可以使用列表返回多个值
print(back())
def back():
    return 1,2,3,"hello world"#元组打包
print(back())
def dis(a,b):
    answer = a*b#answer为局部变量，函数之外无法打印调用，函数出栈被删除
    return answer
#answer=dis(float(input('1:')),float(input('2:')))#在函数外创建的变量为全局变量
#print(answer)
#def change():
#    answer = 20
#    print(answer)#在函数中无法修改全局变量，只能引用全局变量，函数中会创建和全局变量名称相等的局部变量进行操作
#change()
#print(answer)
count = 5
def fun():
    global count#使用global关键字可以使函数引入的全局变量可以改变
    count = 10
    print(count)
fun()
print(count)
def fun1():
    print('fun1被调用')
    def fun2():
        print('fun2被调用')
    fun2()
fun1()#python支持函数嵌套形成递归
#fun2()#报错，在函数内定义的函数在函数外无法调用
def funx(x):
    def funy(y):
        return x*y
    return funy#形成闭包,有参数时添加括号中没有参数时可以不带括号
i = funx(8)
print(i,type(i))#当期i为函数funx
print(i(5))
print(funx(4)(5))#传两次参数，第一次进入funx()第二次执行funy()，有点需要琢磨一下
#先开始执行funx函数，进入后开启return funy再次开始调用funy,执行funyreturn x*y
def fun1():
    x = 5
    def fun2():
        #x=2*x#添加该语句将报错
        x = 2#如果这样使用将不会报错
        x=2*x
        return x#如果直接return x也不会报错
    return fun2()#注意无参数时候带括号直接可以执行
print(fun1())#x相当于外部变量，对于fun2相当于全局变量,而函数在不使用global时无法改变外部变量的值，所以报错
print()
def fun1():
    x = 5
    def fun2():
        #x=2*x#添加该语句将报错
        x = 2#如果这样使用将不会报错
        x=2*x
        return x#如果直接return x也不会报错
    y = fun2()
    return x,y
print(fun1())
'''函数fun2中在调用x=时将创建x变量，而在使用 y=2*x或者其它读取x的语句时
如果前面没有x=相关的语句，将调用全局中x的值，但当改变x值时将在函数内创
建x变量，覆盖全局中x的值，然而在创建x变量时x值时没有的，所以x=2*x会报
错，当使用global时并不会解决问题,因为global对应的是全局变量，然而x只
是fun2的外部变量,而不是全局变量'''
def fun1():
    x = [5]
    def fun2():
        x[0]=2*x[0]#使用列表不会报错，因为列表为容器类型，不会入栈
        return x[0]
    return fun2()
print(fun1())
