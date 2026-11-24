class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat[0])
        best_row = 0
        max_ones = -1

        for i, row in enumerate(mat):
            ones = sum(row)
            if ones > max_ones:
                max_ones = ones
                best_row = i
                if max_ones == n:
                    break

        return [best_row,max_ones]
