class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = [None] * len(words)

        for word in words:
            idx = int(word[-1]) - 1 # 取出結尾數字轉為 0-based 索引
            res[idx] = word[:-1]    # 取出除了結尾數字以外的純單字

        return " ".join(res)
