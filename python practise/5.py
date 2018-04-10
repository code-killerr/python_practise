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
print(mix[0])#取出列表中元素
mix[1]=mix[0]#将列表中第二个元素的值赋给第一个元素
print(mix)
mix.remove(123)#删除和括号中内容相等的元素
print(mix)
del mix[2]#删除相应的元素，del后加列表表示删除列表
print(mix)
a=mix.pop()#pop方法中无参数表示取出最后一个元素，并在列表中删除
print(a,mix)
b=mix.pop(1)#取出第二个元素并删除
print(mix)
print(mix[2:4])#x:y取出列表x-y的元素组成一个列表不包含x
print(mix[:2])#取出0-2的元素不包含标号为2的元素
print(mix[2:])#取出编号为2的元素后的所有元素包含第二个元素