class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 降序排序
        cost.sort(reverse=True)

        total_cost = 0
        for i,c in enumerate(cost):
            # 每第 3 顆糖果（索引 2, 5, 8...）免費，跳過不加
            if (i + 1) % 3 != 0:
                total_cost += c

        return total_cost
