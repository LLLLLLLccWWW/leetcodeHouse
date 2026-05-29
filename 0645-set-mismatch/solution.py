from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        dup = missing = 0
        for i in range(1,len(nums) + 1):
            if count[i] == 2:
                dup = i
            elif count[i] == 0:
                missing = i
        return [dup,missing]
