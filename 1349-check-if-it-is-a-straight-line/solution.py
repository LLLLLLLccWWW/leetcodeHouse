class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        dx = x2 - x1  # 基準斜率的分子
        dy = y2 - y1  # 基準斜率的分母

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            # 交叉相乘，避免除法
            if dy * (x - x1) != dx * (y - y1):
                return False

        return True
