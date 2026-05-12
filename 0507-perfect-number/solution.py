class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        total = 1  # 1 一定是因數
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i           # 加小的因數
                if i != num // i:    # 避免重複加（例如 √num 剛好整除）
                    total += num // i  # 加大的因數
            i += 1

        return total == num
        
