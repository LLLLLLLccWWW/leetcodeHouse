class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        nums = [0] * (n + 1)
        nums[1] = 1

        for idx in range(2, n + 1):
            if idx % 2 == 0:
                nums[idx] = nums[idx // 2]
            else:
                nums[idx] = nums[idx // 2] + nums[idx // 2 + 1]

        return max(nums)
