from collections import Counter
class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        # 1. 最高優先級：Flush (5 張同花色)
        if len(set(suits)) == 1:
            return "Flush"

        # 2. 統計點數出現的最大次數
        max_rank_count = max(Counter(ranks).values())

        # 3. 依據頻率由高至低判定
        if max_rank_count >= 3:
            return "Three of a Kind"
        if max_rank_count == 2:
            return "Pair"

        return "High Card"
