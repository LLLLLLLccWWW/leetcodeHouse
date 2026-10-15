class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        for i in range(n):
            # 1. 檢查第 i 列 (Row)
            if len(set(matrix[i])) != n:
                return False

            # 2. 檢查第 i 行 (Column)
            if len({matrix[r][i] for r in range(n)}) != n:
                return False

        return True
