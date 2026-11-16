from collections import defaultdict
class Solution:
    def similarPairs(self, words: list[str]) -> int:
        seen = defaultdict(int)
        ans = 0

        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            ans += seen[mask]
            seen[mask] += 1

        return ans
