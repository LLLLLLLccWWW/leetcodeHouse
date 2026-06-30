class MyStack(object):

    def __init__(self):
        # 只使用一個佇列
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 1. 取得目前佇列中的元素數量
        size = len(self.queue)

        # 2. 將新元素加入尾端
        self.queue.append(x)

        # 3. 將前面所有舊元素依序彈出並重新放到尾端
        for _ in range(size):
            self.queue.append(self.queue.popleft())
        
    def pop(self):
        """
        :rtype: int
        """
        # 因為經由 push 的處理，最上層的元素已經在佇列的最前端了
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        # 查看佇列最前端的元素
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        # 檢查佇列是否為空
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
