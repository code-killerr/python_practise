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
        
    
    
