from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)

        # 檢查每一個索引 i 的數字 str(i) 出現次數是否等於 int(num[i])
        return all(counts[str(i)] == int(count) for i, count in enumerate(num))
        
