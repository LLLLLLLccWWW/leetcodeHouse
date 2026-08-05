class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        # 2. 取出偶數索引位置的元素並求和 (nums[0], nums[2], nums[4], ...)
        return sum(nums[::2])
