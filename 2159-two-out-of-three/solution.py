class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s1,s2,s3 = set(nums1),set(nums2),set(nums3)
        # 取兩兩交集後聯集
        return list((s1 & s2) | (s2 & s3) | (s3 & s1))
