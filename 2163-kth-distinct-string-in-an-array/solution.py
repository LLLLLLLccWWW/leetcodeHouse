from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # 1. 統計每個字串出現的頻率
        freq = Counter(arr)

        # 2. 依序檢查每個字串
        for s in arr:
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""

