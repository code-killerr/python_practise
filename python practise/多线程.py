import threading
import time
from queue import Queue

a = Queue()#定义queue
b = 0
lock = threading.Lock()
for i in range(1,20):
    a.put(i)
#多线程去除queue的值，造成可以同步的效果
def output(name):
    global b
    while not a.empty():
        print('this is '+ name +' '+ str(a.get()) + time.ctime(time.time()))
        time.sleep(1)
        lock.acquire()
        print('加锁了')
        c = b
        c+= 1
        b = c
        lock.release()
        print('解锁了')
    print('i am out')
# 创建新线程
print(str(threading.active_count()))
a1 = threading.Thread(target = output,args = ('first',))
a2 = threading.Thread(target = output,args = ('second',))

# 开启线程
a1.start()
a2.start()
#join用来判定该线程是否执行完，如果未执行完将阻塞主线程，直至完成
a1.join()
print('a1 is quit')
a2.join()
print('a2 is quit')

print ("退出主线程")