class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total_area = 0

        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    # 1. 加上基礎表面積 (每個正方體 6 個面)
                    total_area += 6 * v
                    # 2. 扣除同位置上下重疊的面 (v - 1 個接觸面，每個接觸面藏 2 個面)
                    total_area -= 2 *(v - 1)

                    # 3. 扣除與上方相鄰位置重疊的面
                    if i > 0:
                        total_area -= 2 * min(v,grid[i - 1][j])

                    # 4. 扣除與左方相鄰位置重疊的面
                    if j > 0:
                        total_area -= 2 * min(v,grid[i][j - 1])

        return total_area
