class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = 1 # 第 0 位元設為 1（1 號朋友初始持球）
        curr = 0
        step = k

        while True:
            curr = (curr + step) % n
            bit = 1 << curr
            if visited & bit:
                break

            visited |= bit
            step += k

        return [i + 1 for i in range(n) if not (visited & (1 << i))]
