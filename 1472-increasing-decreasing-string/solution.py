from collections import Counter
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        res = []

        while len(res) < len(s):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if count[c] > 0:
                    res.append(c)
                    count[c] -= 1
            for c in 'zyxwvutsrqponmlkjihgfedcba':
                if count[c] > 0:
                    res.append(c)
                    count[c] -= 1
        return ''.join(res)
