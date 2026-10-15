class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. 將值與原始索引配對
        indexed_nums = [(num,i) for i,num in enumerate(nums)]

        # 2. 依照數值大小降序排序，取前 k 大元素
        top_k = sorted(indexed_nums,key=lambda x:x[0],reverse=True)[:k]

        # 3. 依照原始索引升序排序，恢復子序列順序
        top_k.sort(key=lambda x: x[1])

        # 4. 提取數值回傳
        return [num for num,_ in top_k]
