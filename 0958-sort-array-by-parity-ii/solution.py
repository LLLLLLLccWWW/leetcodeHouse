class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        even = 0
        odd = 1

        while even < n and odd < n:
            # 如果偶數位置放的是偶數，位置正確，往後跳兩格
            if nums[even] % 2 == 0:
                even += 2
            # 如果奇數位置放的是奇數，位置正確，往後跳兩格
            elif nums[odd] % 2 == 1:
                odd += 2
            # 當偶數位置放了奇數，且奇數位置放了偶數時，進行交換
            else:
                nums[even],nums[odd] = nums[odd],nums[even]
                even += 2
                odd += 2

        return nums
