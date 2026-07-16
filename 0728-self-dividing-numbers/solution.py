class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            temp = num
            while temp > 0:
                digit = temp % 10  # 取得最後一位數
                
                # 如果包含 0，或者無法整除，直接出局
                if digit == 0 or num % digit != 0:
                    return False
                
                temp //= 10  # 去掉最後一位數
            return True
            
        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
                
        return result
