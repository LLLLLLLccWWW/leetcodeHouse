class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        seen_sums = set()

        left,right = 0,len(nums) - 1
        while left < right:
            # 使用兩數之和取代平均值，避免浮點數精確度問題
            seen_sums.add(nums[left] + nums[right])
            left += 1
            right -= 1  

        return len(seen_sums)
