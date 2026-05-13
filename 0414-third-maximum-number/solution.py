class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums),reverse = True) # 去重 + 由大到小排序

        if len(nums) < 3:
            return nums[0]
        
        return nums[2]
        
