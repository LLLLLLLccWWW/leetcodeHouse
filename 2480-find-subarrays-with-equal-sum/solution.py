class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()

        for i in range(len(nums) - 1):
            two_sum = nums[i] + nums[i + 1]
            if two_sum in seen:
                return True
            seen.add(two_sum)

        return False
