class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        # 情況1：最大三個
        case1 = nums[n-1] * nums[n-2] * nums[n-3]
        # 情況2：最小兩個 × 最大一個
        case2 = nums[0] * nums[1] * nums[n-1]

        return max(case1,case2)
