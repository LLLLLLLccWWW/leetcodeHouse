class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        # 先每人發 1 元，問題轉化為用剩餘金額盡可能湊出最多個 7 元
        rem = money - children
        ans = min(children, rem // 7)
        leftover = rem - ans * 7

        # 特例 A：全部小孩都拿到 8 元但錢還沒分完，必須有一人多拿
        if ans == children and leftover > 0:
            ans -= 1
        # 特例 B：只剩最後一人沒拿 8 元，且他剛好拿到 1 + 3 = 4 元，必須拆動一位 8 元小孩
        elif ans == children -1 and leftover == 3:
            ans -= 1

        return ans
