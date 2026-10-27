class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)

        # 1. 分別收集奇數與偶數，並降序排序
        odds = sorted([d for d in s if int(d) % 2 != 0],reverse=True)
        evens = sorted([d for d in s if int(d) % 2 == 0],reverse=True)

        odd_idx,even_idx = 0,0
        res = []

        # 2. 依原本位置的奇偶性，優先填入較大的同奇偶數字
        for d in s:
            if int(d) % 2 != 0:
                res.append(odds[odd_idx])
                odd_idx += 1
            else:
                res.append(evens[even_idx])
                even_idx += 1

        return int("".join(res))
