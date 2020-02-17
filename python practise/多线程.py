import threading
import time
from queue import Queue

a = Queue()#定义queue
for i in range(1,20):
    a.put(i)
#多线程去除queue的值，造成可以同步的效果
def output(name):
    while not a.empty():
        print('this is '+ name +' '+ str(a.get()) + time.ctime(time.time()))
        time.sleep(1)
    print('i am out')
# 创建新线程
print(str(threading.active_count()))
threading._start_new_thread(output,('first',))
threading._start_new_thread(output,('second',))

# 开启新线程
while True:
    if threading.active_count() == 0:
        break;
    time.sleep(1)
print ("退出主线程")