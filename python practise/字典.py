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