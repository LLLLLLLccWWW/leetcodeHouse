from threading import Semaphore

class Foo(object):
    def __init__(self):
        self.sem2 = Semaphore(0)  # 初始為0，second要等
        self.sem3 = Semaphore(0)  # 初始為0，third要等

    def first(self, printFirst):
        printFirst()
        self.sem2.release()  # 通知second可以執行了

    def second(self, printSecond):
        self.sem2.acquire()  # 等待first完成
        printSecond()
        self.sem3.release()  # 通知third可以執行了

    def third(self, printThird):
        self.sem3.acquire()  # 等待second完成
        printThird()
