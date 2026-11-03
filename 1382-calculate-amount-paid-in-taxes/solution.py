class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        total_tax = 0.0
        prev_upper = 0

        for upper,percent in brackets:
            if income <= prev_upper:
                break

            # 計算當前級距所涵蓋的應稅收入
            taxable = min(income,upper) - prev_upper
            total_tax += taxable * (percent / 100.0)

            prev_upper = upper

        return total_tax
