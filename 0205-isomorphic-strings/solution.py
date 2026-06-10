class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 用 zip 比較 index 模式
        return [s.index(c) for c in s] == [t.index(c) for c in t]
