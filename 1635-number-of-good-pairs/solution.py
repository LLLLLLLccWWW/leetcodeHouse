class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        result = 0

        for num in nums:
            result += count.get(num,0)
            count[num] = count.get(num,0) + 1

        return result
