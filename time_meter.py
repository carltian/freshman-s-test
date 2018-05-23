import time as t
class Mytimer():
    def __init__(self):
        self.unit = ['年','月','日','时','分','秒']
        self.promte = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
    def __str__(self):
        return self.promte
    _repr_ = __str__
    def __add__(self, other):
        promte = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                promte += (str(result[index] + self.unit[index]))
        return promte
    def start(self):
        self.begin = t.localtime()
        self.promte = "请先调用stop"
        print("开始计时")
    def stop(self):
        if not self.begin:
            print("请先调用start")
        else:
            self.end= t.localtime()
            self._calc()
            print ("计时结束")
    def _calc(self):
        self.lasted = []
        self.promte = "总共时间是"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.promte += str(self.lasted[index])
            if self.lasted[index]:
                self.promte += (str(self.lasted[index]) + self.unit[index])
        self.begin = 0
        self.end = 0
