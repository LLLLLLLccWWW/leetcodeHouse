class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        count = 0
        col = n - 1 # 指向目前這一列「最後一個非負數」候選位置

        for row in range(m):
            # col 往左移動，直到 grid[row][col] 不是負數（或超出邊界）
            while col >= 0 and grid[row][col] < 0:
                col -= 1
            # col+1 到 n-1 都是負數
            count += n - col - 1

        return count

