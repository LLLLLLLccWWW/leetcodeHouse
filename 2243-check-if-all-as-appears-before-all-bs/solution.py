class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 若存在 "ba"，代表有 'a' 出現在 'b' 後面
        return "ba" not in s
