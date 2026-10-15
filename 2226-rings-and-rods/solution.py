class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        # 1. 建立 10 個桿子的顏色集合
        rods  =[set() for _ in range(10)]

        # 2. 每兩字元為一組解析 (Color, Rod)
        for i in range(0,len(rings),2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)

        # 3. 計算包含 3 種顏色的桿子數量
        return sum(1 for rod_set in rods if len(rod_set) == 3)
