from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = Counter(s)
        # 檢查所有頻率值轉為 Set 後的數量是否為 1
        return len(set(counts.values())) == 1
