class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        min_prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max(1,1 - min_prefix_sum)
