class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        left,right = 0,len(nums) - 1

        while left < right:
            # 計算 nums[right] 對應的 10 的冪次進位乘數
            mult = 10
            while mult <= nums[right]:
                mult *= 10
            ans += nums[left] * mult + nums[right]
            left += 1
            right -= 1

        if left == right:
            ans += nums[left]

        return ans

    
