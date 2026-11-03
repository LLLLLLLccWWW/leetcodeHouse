from collections import Counter
class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)

        pairs = sum(cnt // 2 for cnt in counts.values())
        leftovers = sum(cnt % 2 for cnt in counts.values())

        return [pairs,leftovers]
