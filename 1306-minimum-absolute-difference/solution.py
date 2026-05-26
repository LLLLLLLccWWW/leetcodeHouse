class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # 排序後，最小差值一定在相鄰的兩個數字之間，然後找出所有差值等於最小值的配對。

        arr.sort()

        # 找最小差值
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            min_diff = min(min_diff,arr[i+1] - arr[i])

        # 找所有差值等於最小值的配對
        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i],arr[i+1]])
        return result
            
