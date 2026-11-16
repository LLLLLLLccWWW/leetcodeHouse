class Solution:
    def captureForts(self, forts: list[int]) -> int:
        ans = 0
        prev = -1   # 記錄上一個非零位置 (1 或 -1) 的索引

        for i,val in enumerate(forts):
            if val != 0:
                # 若前一個非零存在，且兩端一為 1 一為 -1（即 val != forts[prev]）
                if prev != -1 and val != forts[prev]:
                    ans = max(ans, i - prev - 1)
                prev = i

        return ans
