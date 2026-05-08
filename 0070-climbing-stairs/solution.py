class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prev1 = 1   # f(n-2)
        prev2 = 2   # f(n-1)
        for i in range(3,n + 1):
            curr = prev1 + prev2    # f(n) = f(n-1) + f(n-2)
            prev1 = prev2
            prev2 = curr
        return prev2
        
