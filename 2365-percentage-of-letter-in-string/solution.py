class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # count * 100 // len(s) 自動進行整數向下取整
        return (s.count(letter) * 100) // len(s)
