class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:  # 不是要移除的值
                nums[k] = nums[i]   # 放到前面
                k+=1    # 位置往後移
        return k
        
