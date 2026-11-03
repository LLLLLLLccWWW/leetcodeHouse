class Solution:
    def countAsterisks(self, s: str) -> int:
        # split('|')[::2] 提取所有不在豎線對內部的子字串
        return sum(part.count('*') for part in s.split('|')[::2])
