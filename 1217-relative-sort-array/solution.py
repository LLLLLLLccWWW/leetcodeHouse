class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = Counter(arr1)
        res = []

        # 1. 按照 arr2 的順序加入元素
        for num in arr2:
            res.extend([num] * count[num])
            del count[num]  # 加完後刪除紀錄

        # 2. 處理剩下的元素：將鍵值排序後依序加入
        remaining = sorted(count.keys())
        for num in remaining:
            res.extend([num] * count[num])

        return res
