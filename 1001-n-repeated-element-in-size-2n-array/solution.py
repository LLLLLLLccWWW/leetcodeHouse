class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # 檢查與前 1、2、3 個位置是否相同
            if i >= 1 and nums[i] == nums[i - 1]:
                return nums[i]
            if i >= 2 and nums[i] == nums[i - 2]:
                return nums[i]
            if i >= 3 and nums[i] == nums[i - 3]:
                return nums[i]

        return -1
