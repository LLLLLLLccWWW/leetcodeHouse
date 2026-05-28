class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        hex_chars = "0123456789abcdef"

        if num < 0:
            num = num + 2**32   # 等同於 num & 0xffffffff

        result = ''
        while num > 0:
            result = hex_chars[num & 0xf] + result  # 取最後4bit
            num >>= 4   # 右移4位

        return result 
