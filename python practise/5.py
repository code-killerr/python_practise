mix = ["sdawe",123,4.56,[1,2,3]]#python具有列表不具有数组，列表可以包括整数，浮点数，字符串，对象,列表等
for i in mix:
    print(i)
empty=[]#允许空列表
print(empty)
mix.append("hello")#append代表在列表结尾添加括号中的内容，不过只能添加一个
print(mix)
mix.extend(["world","OK"])#extend将两个列表拼接起来，括号中的列表插在mix的结尾
print (mix)
mix.insert(0,"yes")#insert可将内容插入到指定位置
print(mix)