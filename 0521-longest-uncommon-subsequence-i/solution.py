class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # 如果兩個字串完全相同，回傳 -1
        if a == b:
            return -1

        # 如果不相同，直接回傳兩個字串長度的最大值
        return max(len(a),len(b))
