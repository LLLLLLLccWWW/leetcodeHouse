class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1    # 特殊情況，0的補數是1
        mask = (1 << n.bit_length()) - 1
        return n ^ mask
