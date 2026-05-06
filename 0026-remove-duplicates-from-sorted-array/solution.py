class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1   # 從1開始，第一個數字一定保留

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:    # 跟前一個不一樣，代表是新的數字

                nums[k] = nums[i]   # 放到前面

                k += 1      # 位置往後移
                
        return k
        
