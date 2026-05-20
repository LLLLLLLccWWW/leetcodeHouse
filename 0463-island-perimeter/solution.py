class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rows,cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                
                    # 檢查上方
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 1
                    # 檢查下方
                    if i < rows-1 and grid[i+1][j] == 1:
                        perimeter -= 1
                    # 檢查左方
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 1
                    # 檢查右方
                    if j < cols - 1 and grid[i][j+1] == 1:
                        perimeter -= 1

        return perimeter

