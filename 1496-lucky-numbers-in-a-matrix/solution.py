class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        # 預先計算每行最小值和每列最大值
        row_mins = [min(row) for row in matrix]
        col_maxs = [max(matrix[r][c] for r in range(len(matrix))) 
                    for c in range(len(matrix[0]))]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = matrix[r][c]
                if val == row_mins[r] and val == col_maxs[c]:
                    result.append(val)

        return result
