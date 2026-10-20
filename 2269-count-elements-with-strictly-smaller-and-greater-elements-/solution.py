class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)

        # 統計嚴格介於最小值與最大值之間的元素數量
        return sum(1 for x in nums if min_val < x < max_val)
