class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 用單指針追蹤 s 的匹配進度，遍歷 t 的每個字元，遇到與 s[i] 相符的就推進指針，最終看是否把 s 全部匹配完。
        i = 0
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1
        return i == len(s)
