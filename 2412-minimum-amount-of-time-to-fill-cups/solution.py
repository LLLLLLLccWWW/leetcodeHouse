class Solution:
    def fillCups(self, amount: list[int]) -> int:
        # max(amount) 代表最大值的瓶頸限制
        # (sum(amount) + 1) // 2 代表兩兩配對下的最小秒數
        return max(max(amount),(sum(amount) + 1) // 2)
