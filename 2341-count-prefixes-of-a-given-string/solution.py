class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        # 計算符合 s.startswith(w) 的字串數量
        return sum(s.startswith(w) for w in words)
