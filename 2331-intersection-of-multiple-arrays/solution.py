class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        # 以第一個子陣列的 set 作為基準
        res_set = set(nums[0])

        # 逐一與後續子陣列求交集
        for arr in nums[1:]:
            res_set.intersection_update(arr)

        return sorted(res_set)
    
