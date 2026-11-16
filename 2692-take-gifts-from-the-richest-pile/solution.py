import heapq
from math import isqrt
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 將元素取負數以利用 heapq 模擬 Max-Heap
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            # 取得當前最大值
            top = -max_heap[0]
            # 若最大值已是 1，後續操作不會再減少禮物，直接提早結束
            if top == 1:
                break
            # 彈出最大值並推入平方根下取整
            heapq.heapreplace(max_heap,-isqrt(top))

        return -sum(max_heap)

