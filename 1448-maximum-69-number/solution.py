class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        # 轉字串，只替換第一個6，再轉回數字
        return int(str(num).replace('6','9',1))
        
