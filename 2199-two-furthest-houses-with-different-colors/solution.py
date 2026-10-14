class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        max_dist = 0

        # 1. 固定左端點 colors[0]，從右往左找第一個不同顏色的房屋
        for i in range(n - 1,-1,-1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist,i)
                break

        # 2. 固定右端點 colors[n-1]，從左往右找第一個不同顏色的房屋
        for i in range(n):
            if colors[i] != colors[-1]:
                max_dist = max(max_dist,n - 1 - i)
                break

        return max_dist
