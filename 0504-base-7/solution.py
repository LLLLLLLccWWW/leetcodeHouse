class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)  # 絕對值
        result = ""

        while num > 0:
            result = str(num % 7) + result  # 餘數加到前面
            num //= 7
        return "-"+ result if negative else result
        
