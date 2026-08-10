class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(set(arr))
        rank = {num: i + 1 for i,num in enumerate(sorted_unique)}
        return [rank[num] for num in arr]
