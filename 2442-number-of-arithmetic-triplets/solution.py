class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        # 建立 HashSet
        num_set = set(nums)
        count = 0

        # 對每個數檢查等差條件
        for n in nums:
            if n + diff in num_set and n + 2 * diff in num_set:
                count += 1

        return count
