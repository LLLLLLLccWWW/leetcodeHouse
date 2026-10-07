class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0

        # 1. 將陣列進行遞增排序
        nums.sort()

        min_diff = float('inf')

        # 2. 檢視所有長度為 k 的連續子陣列
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff
