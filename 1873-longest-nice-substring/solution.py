class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""

        char_set = set(s)

        for i,c in enumerate(s):
            # 若大小寫不同時存在，以此字元進行分割
            if c.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                # 題目要求長度優先，若相同長度則取較早出現者 (left)
                return left if len(left) >= len(right) else right

        return s
