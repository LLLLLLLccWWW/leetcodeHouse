class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 1. 檢查元素總數是否相符
        if len(original) != m * n:
            return []

        # 2. 每 n 個元素切成一列
        return [original[i:i+n] for i in range(0,m*n,n)]
