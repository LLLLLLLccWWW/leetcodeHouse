class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 依照「絕對值」從大到小排序
        nums.sort(key=lambda x: abs(x),reverse=True)

        # 第一階段：優先把絕對值大的負數翻轉成正數
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # 第二階段：如果 k 還沒用完，且剩餘 k 為奇數
        # 翻轉目前絕對值最小的數 (即陣列最後一個元素)
        if k % 2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)
