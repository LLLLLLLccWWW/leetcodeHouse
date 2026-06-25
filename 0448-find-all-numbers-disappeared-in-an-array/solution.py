class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 第一輪：利用正負號標記出現過的數字
        for num in nums:
            # 因為數字可能已經被轉成負數，所以要取絕對值
            index = abs(num) - 1
            # 如果該位置是正數，將其轉為負數，表示這個「對應的數字」存在
            if nums[index] > 0:
                nums[index] = -nums[index]

        # 第二輪：收集所有依然為正數的位置
        result = []
        for i in range(len(nums)):
            # 如果 nums[i] 是正數，代表沒有任何數字對應到索引 i，也就是數字 i + 1 消失了
            if nums[i] > 0:
                result.append(i + 1)

        return result
