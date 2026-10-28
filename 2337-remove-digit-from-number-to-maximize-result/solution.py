class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_idx = -1
        n = len(number)

        for i in range(n):
            if number[i] == digit:
                last_idx = i
                # 貪婪策略：若下一個數字比當前 digit 大，移除當前 digit 能讓數值變大
                if i + 1 < n and number[i] < number[i + 1]:
                    return number[:i] + number[i + 1:]

        # 若沒有觸發貪婪條件，移除最後一個出現的 digit
        return number[:last_idx] + number[last_idx + 1:]
