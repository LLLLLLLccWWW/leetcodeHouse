from collections import Counter
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # 將 nums 壓縮為 (數值, 頻率) 並依數值由大到小排序，便於 num < d 時提前 break
        freq_sorted = sorted(Counter(nums).items(),reverse=True)

        max_score = -1
        best_div = min(divisors)

        for d in set(divisors):
            score = 0
            for num,cnt in freq_sorted:
                if num < d:
                    break
                if num % d == 0:
                    score += cnt

            if score > max_score or (score == max_score and d < best_div):
                max_score = score
                best_div = d

        return best_div
