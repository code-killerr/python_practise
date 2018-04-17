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

