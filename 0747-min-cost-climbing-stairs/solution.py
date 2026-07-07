class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # prev2 代表 dp[i-2]，prev1 代表 dp[i-1]
        # 初始時，站在第 0 階和第 1 階的花費都是 0
        prev2 = 0
        prev1 = 0

        # 從第 2 階一路計算到頂端 (len(cost) + 1)
        for i in range(2,len(cost) + 1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])

            prev2 = prev1
            prev1 = current

        return prev1
