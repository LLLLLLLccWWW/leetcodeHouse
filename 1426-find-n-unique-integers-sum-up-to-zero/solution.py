class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = list(range(1,n))
        # 最後一個數
        res.append(- (n - 1) * n // 2)
        return res
