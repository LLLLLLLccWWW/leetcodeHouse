class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 當 num 為 0 或者末尾不是 0 時回傳 True
        return num == 0 or num % 10 != 0
