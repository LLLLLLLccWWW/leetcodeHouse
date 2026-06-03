class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m,n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        flat = [mat[i][j] for i in range(m) for j in range(n)]

        return [flat[i*c:(i+1)*c] for i in range(r)]
