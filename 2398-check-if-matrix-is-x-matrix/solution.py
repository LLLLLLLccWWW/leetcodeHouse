class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        n = len(grid)

        for r in range(n):
            for c in range(n):
                is_diagonal = (r == c) or (r + c == n - 1)

                # 對角線元素不可為 0，非對角線元素必須為 0
                if is_diagonal and grid[r][c] == 0:
                    return False
                if not is_diagonal and grid[r][c] != 0:
                    return False

        return True
