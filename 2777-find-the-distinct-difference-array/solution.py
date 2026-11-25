from collections import Counter
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        suffix_cnt = Counter(nums)
        suffix_distinct = len(suffix_cnt)
        prefix_mask = 0
        ans = []

        for x in nums:
            prefix_mask |= 1 << x
            suffix_cnt[x] -= 1
            if suffix_cnt[x] == 0:
                suffix_distinct -= 1
            ans.append(prefix_mask.bit_count() - suffix_distinct)

        return ans
