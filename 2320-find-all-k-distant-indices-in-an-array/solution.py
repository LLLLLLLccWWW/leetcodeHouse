class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        r = 0   # 紀錄下一個未被覆蓋的最小索引

        for j in range(n):
            if nums[j] == key:
                # 起點不能小於 j - k，且不能小於當前已被覆蓋到的邊界 r
                start = max(j - k,r)
                end = min(j + k,n - 1)

                for i in range(start,end + 1):
                    res.append(i)

                # 更新已被覆蓋到的最新邊界
                r = end + 1

        return res
