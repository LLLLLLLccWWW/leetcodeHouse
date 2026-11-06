from collections import Counter
class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        weights = Counter()

        # 累加 items1 與 items2 的權重
        for val,weight in items1 + items2:
            weights[val] += weight

        # 依 value 升冪排序後轉換為 [[value, weight], ...]
        return sorted([val,weight] for val,weight in weights.items())
