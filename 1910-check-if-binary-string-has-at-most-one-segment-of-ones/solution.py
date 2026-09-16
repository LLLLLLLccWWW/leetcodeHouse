class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 因為 s[0] 必定是 '1'，若存在 "01" 代表出現了第二個 1 區段
        return "01" not in s
