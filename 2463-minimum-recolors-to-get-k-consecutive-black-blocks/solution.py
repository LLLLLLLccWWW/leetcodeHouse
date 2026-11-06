class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 1. 計算第一個長度為 k 的視窗中的 'W' 數量
        w_count = blocks[:k].count('W')
        min_recolors = w_count

        # 2. 滑動視窗，O(1) 更新 'W' 數量
        for i in range(k,len(blocks)):
            if blocks[i-k] == 'W':
                w_count -= 1
            if blocks[i] == 'W':
                w_count += 1
            min_recolors = min(min_recolors,w_count)

        return min_recolors

