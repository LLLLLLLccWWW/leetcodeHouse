class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        num_set = set(nums)

        # 當前的 original 在集合中時持續翻倍
        while original in num_set:
            original *= 2

        return original
