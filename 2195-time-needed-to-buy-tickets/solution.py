class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        target = tickets[k]
        total_time = 0

        for i,t in enumerate(tickets):
            if i <= k:
                # 排在 k 之前（包含 k 本人），最多買 target 次
                total_time += min(t,target)
            else:
                # 排在 k 之後，最多買 target - 1 次
                total_time += min(t,target - 1)

        return total_time
