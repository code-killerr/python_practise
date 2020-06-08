#lambda为匿名函数，指没有名字的函数,返回的是一个函数,sort接收的参数就是一个内容为返回输入的值的函数
x = 1
y =2
#1.将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。

a = lambda x,y:print(x+y)
a(x,y)

#2.将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。

print = lambda x,y:x*y

#干了点坏事，危险操作蛤

print(2,3)

#3. 将lambda函数作为其他函数的返回值，返回给调用者。
#这个一个典型的闭包

def aaa(value):
    x = value
    def bbb():
        return x+2
    return bbb

#lambda闭包可以这么玩，这个时候就把我们的value固定了起来，用来实现动态参数的固定
    
def aaa(value):
    return lambda x:value+x

#4. 将lambda函数作为参数传递给其他函数。例如字符串排序
a = ['3','1','5','6']
a.sort(key = lambda x:x)
