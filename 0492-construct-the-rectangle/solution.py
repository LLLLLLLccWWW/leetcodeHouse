class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # 從 area 的平方根開始當作寬度 W 的起點
        w = int(math.sqrt(area))

        # 往回找第一個能整除 area 的數
        while area % w != 0:
            w -= 1

        # 找到 W 後，L 自然就是 area // W
        return [area // w, w]
