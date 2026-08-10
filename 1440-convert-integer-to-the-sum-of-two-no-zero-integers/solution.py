class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def has_no_zero(num):
            return '0' not in str(num)

        for a in range(1,n):
            b = n - a
            if has_no_zero(a) and has_no_zero(b):
                return [a, b]
        return []
