class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0

        for i in range(len(timeSeries) - 1):
            # 間隔 vs duration 取較小的
            gap = timeSeries[i+1] - timeSeries[i]
            total += min(gap,duration)

        # 最後一次攻擊一定是完整的 duration
        total += duration

        return total
