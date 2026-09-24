class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1,len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                if count > 1:
                    return False

                # 若 i >= 2 且 nums[i-2] >= nums[i]，則必須刪除 nums[i] (將 nums[i] 修改為 nums[i-1])
                if i >= 2 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]

        return True
