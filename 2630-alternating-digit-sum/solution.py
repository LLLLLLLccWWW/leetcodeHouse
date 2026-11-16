class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        sign = 1

        while n > 0:
            ans += sign * (n % 10)
            sign = -sign
            n //= 10

        # 若總位數為奇數，迴圈結束時 sign 為 -1，-sign 為 +1（保留原值）
        # 若總位數為偶數，迴圈結束時 sign 為 +1，-sign 為 -1（整體變號）
        return -sign * ans 
