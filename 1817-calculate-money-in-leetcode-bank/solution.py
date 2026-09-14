class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        rem = n % 7 

        # 1. 計算完整週的存錢總額 (等差數列和)
        weeks_sum = 28 * weeks + 7 * (weeks - 1) * weeks // 2 

        # 2. 計算剩餘天數的存錢總額
        # 起始金額為 weeks + 1
        rem_sum = sum((weeks + 1) + i for i in range(rem))

        return weeks_sum + rem_sum
