class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 轉成32位元二進位字串（補齊前面的0）
        binary = format(n, '032b')
        # 反轉字串，轉回整數
        return int(binary[::-1], 2)
        
