class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        balance = 0
        for c in s:
            balance += 1 if c == 'R' else -1
            if balance == 0:
                result += 1
        return result
