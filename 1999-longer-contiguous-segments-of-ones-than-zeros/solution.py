class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def maxConsecutive(ch):
            max_count = curr = 0
            for c in s:
                if c == ch:
                    curr += 1
                    max_count = max(max_count,curr)
                else:
                    curr = 0
            return max_count
        
        return maxConsecutive('1') > maxConsecutive('0')
