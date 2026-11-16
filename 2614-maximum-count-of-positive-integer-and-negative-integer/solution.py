from bisect import bisect_left, bisect_right
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        # 第一個 >= 0 的索引即為負數的數量
        neg = bisect_left(nums,0)
        # 第一個 > 0 的索引右側皆為正數
        pos = len(nums) - bisect_right(nums,0)

        return max(neg,pos)
