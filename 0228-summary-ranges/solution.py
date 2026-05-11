class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        result = []
        start = nums[0]     # 記錄每段的起點
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:    # 不連續，結束這段
                if start == nums[i-1]:      # 起點==終點，單一數字
                    result.append(str(start))
                else:                       # 起點!=終點，範圍
                    result.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]             # 開始新的一段
        
        # 處理最後一段
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))
        
        return result 
                    


