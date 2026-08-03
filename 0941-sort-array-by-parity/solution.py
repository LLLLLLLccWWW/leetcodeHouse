class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left,right = 0,len(nums) - 1

        while left < right:
            # 左邊是奇數，右邊是偶數 -> 交換
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            # 左邊已經是偶數，往右前進
            if nums[left] % 2 == 0:
                left += 1

            # 右邊已經是奇數，往左前進
            if nums[right] % 2 == 1:
                right -= 1

        return nums
