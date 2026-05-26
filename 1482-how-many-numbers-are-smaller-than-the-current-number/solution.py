class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)

        # 建立每個數字對應的答案
        rank = {}
        for i,n in enumerate(sorted_nums):
            if n not in rank:   # 只記錄第一次出現的index
                rank[n] = i

        return [rank[n] for n in nums]
