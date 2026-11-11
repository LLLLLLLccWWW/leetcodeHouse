class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # 1. 執行順序操作
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # 2. 雙指標：將非 0 元素前移
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos],nums[i] = nums[i],nums[pos]
                pos += 1

        return nums

