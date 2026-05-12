class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        # 收集所有格子的座標
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append([r,c])
        # 按照距離排序
        cells.sort(key = lambda x: abs(x[0] -rCenter) + abs(x[1] - cCenter))
        return cells
        
