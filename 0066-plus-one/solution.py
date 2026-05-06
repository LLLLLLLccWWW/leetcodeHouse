class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 從最後一位往前掃
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:   # 不是9，直接+1，結束
                digits[i] += 1
                return digits   
            digits[i] = 0       # 是9，變成0，繼續往前進位
        return [1] + digits
