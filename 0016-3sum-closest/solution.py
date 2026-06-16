class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 排序，方便雙指針判斷方向
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        # 固定 nums[i]，雙指針找另外兩數
        for i in range(n - 2):
            l,r = i + 1,n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # . 更新最接近的總和
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total == target:
                    return total
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return closest
