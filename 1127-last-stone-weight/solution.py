import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]  # 全部變負數
        heapq.heapify(heap)          # 建立heap

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # 最重的石頭
            x = -heapq.heappop(heap)  # 第二重的石頭

            if x != y:
                heapq.heappush(heap, -(y - x))  # 剩餘的放回去

        return -heap[0] if heap else 0
