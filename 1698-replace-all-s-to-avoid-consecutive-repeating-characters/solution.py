class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        n = len(chars)

        for i in range(n):
            if chars[i] == '?':
                for c in 'abc':
                    left_ok = (i == 0 or chars[i - 1] != c)
                    right_ok = (i == n - 1 or chars[i + 1] != c)
                    if left_ok and right_ok:
                        chars[i] = c
                        break
                        
        return ''.join(chars)
