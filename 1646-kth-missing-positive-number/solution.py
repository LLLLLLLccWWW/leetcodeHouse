class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr_idx = 0
        current = 1

        while k > 0:
            if arr_idx < len(arr) and arr[arr_idx] == current:
                arr_idx += 1
            else:
                k -= 1
                if k == 0:
                    return current
            current += 1
            
        return current
