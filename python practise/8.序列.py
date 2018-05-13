'''可以通过索引得到每一个元素
    默认索引值从0开始
    可以通过分片方法得到一个范围内元素集合
    具有很多共同操作符
    满足以上几点统称为序列
'''
#1.list()把一个可迭代对象转换为列表
a=list()#无参数生成空列表
print(a)
b='hello world'
b=list(b)#将字符串每一个字符迭代为列表
print(b)
#2.tuple([iterable])将可迭代对象转换为元组同list()
#3.str(obj)将obj对象转换为字符串
#len(sub)返回sub长度
print(len(b))
#4.max()返回序列或者参数集合中最大值
print(max(1,2,3,4,5))
print(max(b))#以ascii码顺序排列找到最大值
#4.min()返回序列或参数中最小值
print(min("helloworld"))
c=[1,2,3,4,'c']
#print(max(c))#报错，类型不一样，使用max和min时类型应相同
#5.sum(iterable[,start=0])#返回序列iterable和可选参数start的总和
d = (4,2,1,2,3)
print(sum(d))#将d中值相加，相加类型必须为整数或浮点数数据类型
print(sum(d,8))#将加入第二个参数
#6.sorted按从小到大顺序排列列表
print(sorted(b))
#7.reversed(numbers)#返回迭代器对象,从大到小排列
print(reversed(b))
print(list(reversed(b)))
#8.enumerate()枚举，使用时返回对象
print(list(enumerate(b)))#每个元素变为元组，第一个元素为其所在位置
#9.zip返回由各个参数序列组成的元组的对象
print(list(zip(b,d)))#将两个相同位置的对象打包生成元组





