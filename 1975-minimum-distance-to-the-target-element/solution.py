class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')

        for i,num in enumerate(nums):
            if num == target:
                min_dist = min(min_dist,abs(i - start))
                # 距離不可能小於 0，若達到 0 可提前結束
                if min_dist == 0:
                    return 0

        return min_dist
