class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # i 的1的個數 = (i//2) 的1的個數 + i的最後一位
        dp = [0] * (n + 1)

        for i in range(1,n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
        
