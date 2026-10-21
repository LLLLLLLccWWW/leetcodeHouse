class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 計算 num 自身的各位數之和
        digit_sum = sum(int(d) for d in str(num))


        # 若位數和為偶數，答案為 num // 2；否則為 (num - 1) // 2
        return num // 2 if digit_sum % 2 == 0 else (num-1) // 2
