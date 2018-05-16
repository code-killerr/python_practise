class Pyclass(list):#python中类名约定以大写字母开头,括号中为继承的类
    color = 'red'
    name = 'python'
    
    def printf(self):#声明方法
        print('name')
    def color(self):
        print('color')
P1 = Pyclass()#生成对象
P1.printf()
P1.color()
P1.append(3)
P1.append(4)
print(P1)