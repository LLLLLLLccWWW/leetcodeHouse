class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)

        m1, m2 = min(nums1),min(nums2)
        return min(m1,m2) * 10 + max(m1,m2)
