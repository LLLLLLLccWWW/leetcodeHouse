class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones = s.count('1')

        zeros = 0   # 左段中 0 的個數
        ones = total_ones   # 右段中 1 的個數
        max_score = 0

        for i in range(len(s) - 1):     # 切割點在 i 和 i+1 之間，右段不能為空所以不含最後一個字元
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            max_score = max(max_score, zeros + ones)

        return max_score

