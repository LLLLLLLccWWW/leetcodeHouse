class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = [0] * 100
        result = 0
        for a,b in dominoes:
            # 標準化：小的在前，大的在後
            code = a * 10 + b if a <= b else b * 10 + a
            result += count[code]   # 之前出現過幾次，就能新增幾對
            count[code] += 1
        return result
