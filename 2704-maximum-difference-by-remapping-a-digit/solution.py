class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # 1. 最大值：找到最左側第一個非 '9' 的數位，全部替換為 '9'
        max_val = num
        for ch in s:
            if ch != '9':
                max_val = int(s.replace(ch,'9'))
                break

        # 2. 最小值：直接將最高位數位全部替換為 '0'（題目允許前導零）
        min_val = int(s.replace(s[0],'0'))

        return max_val - min_val
