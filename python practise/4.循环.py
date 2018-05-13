print(3/5)
print(3//5)#python具有整数运算符
print(3**2)#**代表指数，3的二次方为3**2
print(0 and 1)#and代表与操作符
print(0 or 1)#or代表或操作符
print(3<4<5)#解释为3<4 and 4<5
#优先级 **>(+x,-x(正负号))>(*,/,//,+,-)> (<,>,<=,>=,==,!=)>(not and or)
a=1
b=3
if a==b:
    print("ok")
else:
    if(a>b):
        print("a>b")
    else:
        if(a<b):
            print("a<b")
#python使用缩进代替大括号，ifelse语句中不能使用else if需使用elif
if a==b:
    print("ok")
elif a<b:
    print("a<b")
c=a if a<b else b#三元操作符表示a<b为真时c=a否则等于b
#assert 3>4#assert表示断言，当assert后条件为假时终止程序，抛出异常，如若为真无影响
while a<5:#while循环
    a+=1
    print (a)
#for 目标 in 表达式,表达式可为列表，元组等，for循环可以自动遍历其中元素
d="abcdefg"
for i in d:
    print(i)
#range配合for使用range([start,]stop[,step=1])]方括号参数表示可选
for i in range(10):
    print(i)#如果不指定方括号中参数，range中start默认0 step默认1
for i in range(1,10,2):#代表从1开始步长为2
    print(i)
#break代表终止循环，continue代表跳过后面语句进行循环

 
