class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = (1 << num.bit_length()) - 1   # 產生全1的遮罩
        return num ^ mask
