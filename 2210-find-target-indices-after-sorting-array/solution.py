class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_count = 0
        target_count = 0

        # 統計小於 target 與等於 target 的數量
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                target_count += 1

        # 產生相對應的索引範圍 [less_count, less_count + target_count)
        return list(range(less_count,less_count + target_count))
