class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = -1
        second_val = -1
        max_index = -1

        # 單次遍歷，同時找出最大值、最大值索引、以及第二大值
        for i,num in enumerate(nums):
            if num > max_val:
                # 當前數字比最大值還大，原最大值退位變成第二大值
                second_val = max_val
                max_val = num
                max_index = i
            elif num > second_val:
                # 當前數字沒有超越最大值，但比第二大值大，更新第二大值
                second_val = num

        # 檢查最大值是否至少是第二大值的兩倍
        if max_val >= second_val * 2:
            return max_index
        else:
            return -1
        
