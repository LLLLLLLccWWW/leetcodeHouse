class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 初始化 F(0) 和 F(1)
        a,b = 0,1

        # 從 2 計算到 n
        for _ in range(2,n + 1):
            # 新的數等於前兩個數相加
            current = a + b
            # 滾動更新變數
            a = b
            b = current

        return b
