class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        digit_sum = 0

        while n > 0:
            digit_sum += n % k  # 取出 k 進位下的當前最低位數
            n //= k             # 移位，處理下一位數
        return digit_sum
