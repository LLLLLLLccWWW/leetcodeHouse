class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_index = {}
        max_len = -1

        for i, c in enumerate(s):
            if c in first_index:
                max_len = max(max_len, i -first_index[c] - 1)
            else:
                first_index[c] = i

        return max_len
