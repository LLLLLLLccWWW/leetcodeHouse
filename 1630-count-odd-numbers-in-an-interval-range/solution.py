class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def count_odds_up_to(n):
            return (n + 1) // 2

        return count_odds_up_to(high) - count_odds_up_to(low - 1)
