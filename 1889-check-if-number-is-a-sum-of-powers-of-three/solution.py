class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:        #三進位某一位是2，代表需要重複使用
                return False
            n //= 3

        return True
        
