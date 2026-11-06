class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        # 初始化 (n - 2) x (n - 2) 的結果矩陣
        max_local = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                # 提取 3x3 子矩陣的最大值
                max_val = max(
                    grid[r][c]
                    for r in range(i,i + 3)
                    for c in range(j,j + 3)
                )
                max_local[i][j] = max_val

        return max_local
