class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 1. 轉換 HH:MM 為自 00:00 起的總分鐘數
        cur_m = int(current[:2]) * 60 + int(current[3:])
        cor_m = int(correct[:2]) * 60 + int(correct[3:])

        diff = cor_m - cur_m
        ops = 0

        # 2. 依序盡可能選擇最大增量 [60, 15, 5, 1]
        for step in [60,15,5,1]:
            ops += diff // step
            diff %= step

        return ops
