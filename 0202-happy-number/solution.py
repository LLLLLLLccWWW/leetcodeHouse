class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()    # 記錄出現過的數字
        while n != 1:
            if n in seen:   # 出現過了，代表進入循環
                return False
            seen.add(n)     # 記錄這個數字

            # 計算每個位數的平方和
            total = 0
            while n > 0:
                digit = n % 10  # 取個位數
                total += digit ** 2 # 平方後加總
                n = n // 10 # 去掉個位數
            n = total 
        return True     # n == 1，是 Happy Number

