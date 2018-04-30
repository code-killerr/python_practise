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
