class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0

        for i in range(len(s) - k + 1):
            sub_val = int(s[i:i + k])
            # 1. 不能為 0
            # 2. 能整除 num
            if sub_val != 0 and num % sub_val == 0:
                count += 1

        return count
