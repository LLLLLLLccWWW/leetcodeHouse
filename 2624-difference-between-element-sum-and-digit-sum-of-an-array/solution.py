class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ans = 0

        for num in nums:
            ans += num
            while num > 0:
                ans -= num % 10
                num //= 10

        return ans
