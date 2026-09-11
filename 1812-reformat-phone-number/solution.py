class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        # 1. 過濾出所有數字
        digits = [c for c in number if c.isdigit()]

        blocks = []
        i = 0
        n = len(digits)

        # 2. 依照規則分組
        while n - i > 4:
            blocks.append(''.join(digits[i:i+3]))
            i += 3

        # 處理最後剩餘 <= 4 個數字的情況
        rem = n - i
        if rem == 4:
            blocks.append(''.join(digits[i:i+2]))
            blocks.append(''.join(digits[i+2:i+4]))
        else:   # rem == 2 或 rem == 3
            blocks.append(''.join(digits[i:]))

        # 3. 用連字號 '-' 拼接
        return "-".join(blocks)
