from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)

        # 針對 target 中的每個字元，計算 s 能涵蓋幾份，並取最小值
        return min(s_counts[ch] // count for ch, count in target_counts.items())
        
