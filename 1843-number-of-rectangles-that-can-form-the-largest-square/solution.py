class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        max_len = 0
        count = 0

        for l,w in rectangles:
            side = min(l,w)
            if side > max_len:
                max_len = side
                count = 1   # 找到更大邊長，重置計數
            elif side == max_len:
                count += 1  # 邊長相同，計數加 1

        return count
