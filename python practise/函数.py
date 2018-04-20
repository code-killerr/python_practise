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
answer=dis(float(input('1:')),float(input('2:')))#在函数外创建的变量为全局变量
print(answer)
def change():
    answer = 20
    print(answer)#在函数中无法修改全局变量，只能引用全局变量，函数中会创建和全局变量名称相等的局部变量进行操作
change()
print(answer)
