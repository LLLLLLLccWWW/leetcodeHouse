class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # 計算每一列的 sum，並取最大值 max
        return max(map(sum,accounts))
