class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = math.gcd(a,b)
        ans = 0
        # 試除法統計 gcd(a, b) 的因數個數
        i = 1
        while i * i <= g:
            if g % i == 0:
                ans += 1
                if i * i != g:
                    ans += 1

            i += 1

        return ans

