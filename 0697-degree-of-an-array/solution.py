from collections import defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        first = {}
        last = {}

        for i,n in enumerate(nums):
            count[n] += 1
            if n not in first:
                first[n] = i
            last[n] = i

        degree = max(count.values())

        return min(
            last[n] -first[n] + 1 for n in count if count[n] == degree
        )
