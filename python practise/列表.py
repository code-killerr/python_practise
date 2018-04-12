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
print(mix[2:])#取出编号为2的元素后的所有元素包含第二个元素,不加代表取出列表
list1=[321,123]
list2=[123,321]
print(list1>list2)#输出true，比较第0个元素大小
print(list1+list2)#+号可以将两个列表整合起来，相当于extend,extend更规范，用加号无法加入元素
print(list1*3)#*号代表复制列表多少次
print(123 in list1)#返回true表示list1中具有123
print(123 not in list1)#返回flase表示123在list1中，但无法判断列表中列表中的元素
print(1 in mix)#返回flase
print(1 in mix[1])#返回true表示列表mix中的列表具有1
print(list1.count(123))#统计某元素出现次数
list1=list1+list2
list1*=3
print(list1.index(123,3,7))#表示在3-7的元素中123第一次出现的位置
print(list2)
list2.reverse()#翻转列表
print(list2)
list3=[231,2,21312,23]
print(list3)
list3.sort()#从小到大排列
print(list3)
list3.sort(reverse=True)#从大到小
print(list3)
list4=list3[:]#拷贝列表注意使用[:]
list5=list3#这样并不是拷贝，只是给list3的列表起了个新名字
list3.sort()
print(list3)
print(list4)
print(list5)
#元组，无法修改元素的列表
tuple1=(1,"231",23,42)
print(tuple1)#拷贝操作一致[ : ]
#tuple1[0]=3#报错，无法修改元素
temp=1,#逗号代表元组，不加中括号带逗号的为元组
print(type(temp))
temp1=()#空元组
print(type(temp1))
print(4*(4,),4*(4))#元组的重复
tuple1=tuple1[:2]+("hello",)+tuple1[2:]#元组元素的添加,举一反三元组的删除及其它操作
print(tuple1)
del tuple1#删除元组，不经常用，python具有垃圾回收机制，del多为删除标签作用




