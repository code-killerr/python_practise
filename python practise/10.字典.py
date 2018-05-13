#字典中具有key(字典中的元素)和value(其代表的意义)
#字典为python中唯一的映射类型，映射为在两个元素集中存在一对一或一对多的关系
dict1 = {'小a':'小明','小b':'小强','小c':'小丽'}#大括号表示为字典，字典为映射类型,定义为XX:YY,其中XX为key而YY为value，一套的XX:YY称为一套
print("听说你昨天见到了",dict1['小a'])#字典的调用
dict2 = {1:'one',2:'two'}#字典项中的数据可以为整形，浮点型，字符串等类型
print(dict2[2])
dict3 = {}#创建空字典
print(dict3)#help(dict)可以查到dict各种用法
dict3 = dict([('a',1),['b',2],('c',3)])#因为该用法中只允许一个参数，所以在括起所有元组伪装成一个参数使用，中括号中可以不止为元组中括号亦可以改为小括号，成为元组，具有映射关系的数据都可以
print(dict3)
dict4 = dict(b='hello world',a='hello python')#可以用该方法创建字典,注意该方法等号两边应均为不带引号的字符或字符串
print(dict4)
dict4['c']='hello'#增加字典中的数据
print(dict4)
#dict()为工厂函数，可以认为是一种类型，str(),int(),list(),tuple()都属于工厂函数
print(dict1.fromkeys((1,2,3)))#fromkeys(s[,v]),v可选，v为生成字典key对应的value，该函数将生成相应的字典
print(dict1.fromkeys((1,2,3),'hello'))#在后面增加值后可以将其中所有key的value值改为函数中的参数
print(dict1)#使用fromkeys不会更改原来的字典
for key in dict1.keys():#.keys将显示字典中的key
    print(key)#同样.values将显示字典中的value
for item in dict1.items():#.items会调出字典中的项
    print(item)
print(dict1.get('小d','没有啊'))#如果调用get如果输入字典中不存在的key没有第二个参数会返回none,如果有第二个参数将返回第二个参数
print('小a' in dict1)#使用in或者not in可以查看字典中是否具有某key
dict1.clear()#清空字典
print(dict1)
a = dict2#可以使用dict1={}清空字典但是在内存中不会清空，如果有指向它的变量仍可以查看，但是clear会从内存中清空
dict2={}
print(dict2,a)
dict2=a
b=a.copy()#copy可以执行弱拷贝，将a的内容拷贝给b
a.clear()
print(id(a),id(b),id(dict2))
print(a,dict2,b)#可以发现使用clear后b的值仍然存在
print(b)
print(b.pop(2))#弹出括号中key以及其的value
print(b)
print(dict3)
print(dict3.popitem())#弹出字典最后的项
print(dict3)
dict3.setdefault('f')
print(dict3)
dict3.setdefault('h',8)
print(dict3)#setdefault可以在字典中添加项
print(dict4)
dict4.update({'c':'hello py'})#可以使用udate更新字典中key对应的值
print(dict4)
num={}
print(type(num))#字典类型
num={1,2,3,4}
print(type(num),num)#集合类型，集合类型和字典类型区分主要是集合没有映射关系
#print(num[2])#报错，集合是无序的
set1 = set([5,4,3,2,1,1,2])#集合中的工厂函数，集合会去除其中重复元素,集合中需要列表类型的，这样才能去重
print(set1)#集合会自动从小到大排序
print(1 in set1,'1'in set1)#集合同样可以用in判断某元素是否在集合中
set1.add(7)#添加元素
print(set1)
set1.remove(5)#移除元素
print(set1)
set2 = frozenset([1,2,3,4,5])#使用frozenset生成不可变集合
#set2.add(4)#报错，因为集合不可变
