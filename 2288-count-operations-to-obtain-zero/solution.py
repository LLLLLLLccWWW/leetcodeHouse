class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ans = 0
        while num1 > 0 and num2 > 0:
            if num1 < num2:
                num1,num2 = num2,num1
                # num1 >= num2，計算可以連續減去多少次 num2
            ans += num1 // num2
            num1 %= num2
        return ans
