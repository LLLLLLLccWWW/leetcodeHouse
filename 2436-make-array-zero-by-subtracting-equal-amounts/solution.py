class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # 統計 nums 中所有大於 0 的不重複數字數量
        return len({x for x in nums if x > 0})
