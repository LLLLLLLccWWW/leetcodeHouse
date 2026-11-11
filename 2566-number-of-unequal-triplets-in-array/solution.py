from collections import Counter
class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 0
        left_count = 0
        n = len(nums)

        for count in freq.values():
            right_count = n - left_count - count
            ans += left_count * count * right_count
            left_count += count

        return ans
