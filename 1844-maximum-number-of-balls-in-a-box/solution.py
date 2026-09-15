from collections import Counter
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        # 最大的位數和是 99999 -> 9 * 5 = 45，因此陣列大小取 46
        boxes = [0] * 46

        for ball in range(lowLimit,highLimit + 1):
            box_num = 0
            temp = ball
            while temp > 0:
                box_num += temp % 10
                temp //= 10
            boxes[box_num] += 1

        return max(boxes)
