#bbs.fish.com/thread-45814-1-1.html  异常列表
#1.AssertionError 断言assert失败
#assert 3>4
#AttributeError 尝试访问未知对象属性，引用未定义及不存在的东西会报错
#list=[1,2,3,4]
#list1.aaaa
#IndexError 访问未知区域
#print(list[4])
#KeyError 调用查找字典中不存在的关键字
#使用get方法可屏蔽异常
#NameError 调用不存在的变量
#print(x)
#SyntaxError 语法错误
#print 'aaa'
#TypeError 不同类型间无效操作
#1+‘1’
#ZeroDivision 除数为0报错
#try-except
'''
try:
    检测范围
except Exception[as reason]:
    出现异常(Exception)后处理的代码
'''
try:
    f = open('aaaaa.txt')
    print(f.read())
    f.close()
    print('bbbbb')
except OSError:
    print('无法找到文件')
print('aaaaa')
#不会出现红标报错无法继续运行的情况,但是try里面语句将不再执行
try:
    #b = int('b')#未声明异常的语句会红色报错
    a = 1+'1'
    f = open('aaaaa.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件错误，错误情况:'+str(reason))
except TypeError as reason:
    print('类型错误，错误情况:'+str(reason))
#同上，在第一条语句出错后检测出来抛出异常以后不会继续执行try里面的语句
try:
    a = 1+'1'
    b = int('b')
    printf('aaa')
except:
    print('出错了')#任何异常都会抛出该语句，并不推荐使用，会隐藏bug
#except可以包含多个异常
try:
    a = 1+'1'
    f = open('aaaaa.txt')
except (OSError,TypeError) as reason:
    print('文件错误，错误情况:'+str(reason))
#try-finally,无论如何都会执行finally中代码
try:
    f = open('aaa.txt','a')
    print(f.write('bbbbb'))
    #sum = 1+'1'
except OSError as reason:
    print('文件出错:'+str(reason))
finally:
    f.close()#使用finally可以确保文件出错后仍然可以缓存数据进入文件
#其实写在except外也可以执行诶
#raise,可以用来手动引入异常
raise ZeroDivisionError('除数为0')#raise后面跟的是异常名称，不能随便写