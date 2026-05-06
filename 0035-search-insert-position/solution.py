class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # 取中間位置
            
            if nums[mid] == target:
                return mid              # 找到了
            elif nums[mid] < target:
                left = mid + 1          # target 在右半邊
            else:
                right = mid - 1         # target 在左半邊
        
        return left  # 找不到，left 就是應該插入的位置
