class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # 從右向左反向尋找第一個奇數數字
        for i in range(len(num) - 1,-1,-1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]

        return ""
