class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        xy_area = 0
        yz_area = 0
        zx_area = 0

        for i in range(n):
            row_max = 0
            col_max = 0
            for j in range(n):
                # 1. xy 平面：只要有立方體 (v > 0) 就佔用 1 個單位面積
                if grid[i][j] > 0:
                    xy_area += 1
                
                # 2. yz 平面：找第 i 列的最大值
                row_max = max(row_max,grid[i][j])

                # 3. zx 平面：找第 i 欄的最大值 (注意是 grid[j][i])
                col_max = max(col_max,grid[j][i])

            yz_area += row_max
            zx_area += col_max

        return xy_area + yz_area + zx_area
