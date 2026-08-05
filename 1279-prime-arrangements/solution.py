class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2,int(x**0.5) + 1):
                if x % i == 0:
                    return False

            return True

        # 1. 計算 1 到 n 之間的質數個數 P
        p_count = sum(1 for i in range(1,n + 1) if is_prime(i))

        # 2. 非質數個數為 n - p_count
        non_p_count = n - p_count

        # 3. 計算 P! * (n - P)! % (10^9 + 7)
        ans = (math.factorial(p_count) * math.factorial(non_p_count)) % MOD

        return ans
