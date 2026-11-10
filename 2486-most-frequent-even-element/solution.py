from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        # 1. 僅統計偶數的出現頻率
        even_counts = Counter(x for x in nums if x % 2 == 0)

        # 2. 若完全沒有偶數，回傳 -1
        if not even_counts:
            return -1

        # 3. 雙重條件：頻率最高 (-count 最小)，若頻率相同則數字最小 (val 最小)
        return min(even_counts.keys(),key=lambda val:(-even_counts[val],val))
