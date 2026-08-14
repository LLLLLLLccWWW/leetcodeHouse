class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldiers = [(sum(row),i) for i, row in enumerate(mat)]
        soldiers.sort()
        return [i for _, i in soldiers[:k]]
