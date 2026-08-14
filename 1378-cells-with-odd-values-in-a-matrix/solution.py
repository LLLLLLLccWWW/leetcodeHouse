class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row_count = [0] * m
        col_count = [0] * n

        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        odd_rows = sum(1 for x in row_count if x % 2 == 1)
        odd_cols = sum(1 for x in col_count if x % 2 == 1)
        even_rows = m - odd_rows
        even_cols = n - odd_cols

        return odd_rows * even_cols + even_rows * odd_cols

