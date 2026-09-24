import math
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        # 列舉所有可能的 a 和 b
        for a in range(1,n + 1):
            for b in range(1,n + 1):
                sum_sq = a ** 2 + b ** 2
                c = int(math.sqrt(sum_sq))

                # 檢查 c 是否恰好為完全平方根，且 c <= n
                if c ** 2 == sum_sq and c <= n:
                    count += 1

        return count
