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
assert 3>4#assert表示断言，当assert后条件为假时终止程序，抛出异常
