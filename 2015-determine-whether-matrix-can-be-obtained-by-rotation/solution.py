class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        # 旋轉 90 度技巧：zip(*mat[::-1])
        for _ in range(4):
            if mat == target:
                return True
            # 順時針旋轉 90 度
            mat = [list(row) for row in zip(*mat[::-1])]

        return False
