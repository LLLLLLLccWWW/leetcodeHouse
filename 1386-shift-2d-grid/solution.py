class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m,n = len(grid),len(grid[0])
        total = m * n
        k %= total  # 移動超過總格數等於繞圈，取模避免無效重複

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_idx = (idx + k) % total
                new_i,new_j = new_idx // n, new_idx % n
                result[new_i][new_j] = grid[i][j]

        return result
