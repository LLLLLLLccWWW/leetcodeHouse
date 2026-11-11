class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        # 若僅包含數字，轉為 int(s)；否則取字串長度 len(s)
        return max(int(s) if s.isdigit() else len(s) for s in strs)
