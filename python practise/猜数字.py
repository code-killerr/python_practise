import random#引入第三方库
secret = random.randint(1,10)#表示取1到10中间的数
print("-------guess number-------")
num=0
temp = int(input("guess a number:"))
while temp!=secret and num<6:#and操作符相当于&&
    if temp<secret:
        print("too small")
    else:
        print("too large")
    temp = int(input("wrong number,try again："))#python不允许在表达式中赋值
    num+=1#python不允许++
    if temp==secret:
        print("you are right!")
    else:#python else if 注意缩进否则报错，这样格式更加清晰
        if num==6:
            print("you are wrong too many times")
        
print("game over")
"""python中变量是以内容为准，而在c中是以变量为准，c中只要定义变量即分配空间，但是python
变量中只要内容一定，及为改内容分配ID，ID是固定的但是变量名可以不同，一个变量可以拥有多个名称
例如变量为5，对于5会有特定ID,如若a=5而b=5则二者虽然变量名不同，但是ID相同，当改变
了5这个ID的内容是不允许的，所以只能改变变量指向的ID如a+=5或a=1+5这时a的ID发生变化，a成为了新值的名称
  对于 python,拥有整数池，默认1-256，赋值取其中的整数对象，但是不在1~256中的除外,但是仍然无法使用a++
  操作符，++代表为改变对象本身，而+=代表改变变量，在python中存在++i但是意思可以理解为+(+i)相当于给变量
  进行改变正负的操作"""
    
    
