class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 1. 將 4 個位數提取出來並進行升序排序
        digits = sorted(int(d) for d in str(num))

        # 2. 最小的兩個數 (digits[0], digits[1]) 作為十位數
        #    較大的兩個數 (digits[2], digits[3]) 作為個位數
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
