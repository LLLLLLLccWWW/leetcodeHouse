class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xs = sorted(p[0] for p in points)
        max_width = 0

        for i in range(1,len(xs)):
            max_width = max(max_width,xs[i] - xs[i - 1])

        return max_width
