class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 利用 Python 單字元字典序與 ASCII 順序一致的特性，完全避免切片與 int() 轉型
        return sum(1 for s in details if s[11] > '6' or (s[11] == '6' and s[12] > '0'))
