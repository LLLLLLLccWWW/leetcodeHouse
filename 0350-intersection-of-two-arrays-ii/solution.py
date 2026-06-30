class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 為了省空間，確保第一個參數是較短的陣列
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)

        # 統計較短陣列的數字頻率
        counts = Counter(nums1)
        result = []

        # 遍歷較長的陣列
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1    # 消耗一次配對機會

        return result
