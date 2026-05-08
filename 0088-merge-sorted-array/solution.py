class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1        # nums1 最後一個有效數字的位置
        j = n - 1        # nums2 最後一個數字的位置
        k = m + n - 1    # 填入位置，從最後面開始

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i] # nums1 較大，放到後面
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # nums2 還有剩，直接填入（nums1剩的不用管，本來就在那）
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

