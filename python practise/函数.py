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


