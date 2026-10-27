class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1,set2 = set(nums1),set(nums2)

        # set1 - set2 代表在 set1 但不在 set2 的元素
        # set2 - set1 代表在 set2 但不在 set1 的元素
        return [list(set1 - set2),list(set2 - set1)]
