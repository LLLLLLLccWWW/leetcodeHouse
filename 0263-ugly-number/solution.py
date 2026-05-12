class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        
        for factor in [2,3,5]:
            while n % factor == 0:      # 能整除就一直除
                n //= factor
        return n==1     # 最後剩1才是ugly number
        
