class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0   # 下一個非零數字要放的位置
        
        # 第一步：把非零的全部移到前面
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] =nums[i]
                k+=1
        # 第二步：剩下的位置全部補 0
        for i in range(k,len(nums)):
            nums[i] = 0
            
        
