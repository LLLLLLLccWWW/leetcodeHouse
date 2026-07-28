class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        diff = max(nums) - min(nums) -2 * k
        return max(0,diff)

