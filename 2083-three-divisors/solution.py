class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p = int(math.sqrt(n))

        if p < 2 or p * p != n:
            return False

        for i in range(2,int(math.sqrt(p)) + 1):
            if p % i == 0:
                return False

        return True
