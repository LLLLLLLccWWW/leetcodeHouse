class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_dist = float('inf')
        min_idx = -1

        for i,(px,py) in enumerate(points):
            # 檢查是否為合法點 (共享 X 或 Y 座標)
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)
                # 只有當距離嚴格小於當前最小值時才更新，確保 index 最小
                if dist < min_dist:
                    min_dist = dist
                    min_idx = i

        return min_idx
