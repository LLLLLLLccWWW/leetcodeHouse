class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_seen = [-1]*26

        for i,ch in enumerate(s):
            idx = ord(ch) - ord('a')

            # 若為首次出現，記錄當前索引
            if first_seen[idx] == -1:
                first_seen[idx] = i
            else:
                # 第二次出現，驗證兩者間距是否等於 distance[idx]
                actual_dist = i - first_seen[idx] - 1
                if actual_dist != distance[idx]:
                    return False

        return True
