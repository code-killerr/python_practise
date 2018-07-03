import time as t#在调用time库时可以直接用t代替
class Count_Time():
    def __init__(self):
        self.message = "未开始计时"
        self.count = 0
        self.sta = 0
        self.sto = 0
        self.data = ['年','月','日','时','分','秒']
    def start(self):#开始
        self.sta = t.localtime()
        print("计时开始")
    def stop(self):#结束
        if self.sta!=0:
            self.sto = t.localtime()
            print("计时结束")
        else:
            print("先开始调用start")
        self.acount()
    def acount(self):
        self.count = []
        if self.sta != 0 and self.sto != 0:
            self.message = "运行了："
            for i in range(6):
                self.count.append(self.sto[i]-self.sta[i])
                if self.count[i] != 0:
                    self.message += str(self.count[i])+self.data[i]#计算经过的时间
            self.sta = 0
            self.sto = 0#初始化
        if self.sta != 0 and self.sto == 0:
            self.message = "请先停止后再计时"
    def __str__(self):
        return self.message
    def __add__(self,other): 
        self.ResultMessage = "总共运行了:"
        for i in range(6):
           result = self.count[i]+other.count[i]
           if result != 0:
               self.ResultMessage += str(result)+self.data[i]#计算经过的时间
        return self.ResultMessage
    __repr__ = __str__
a = Count_Time()
    