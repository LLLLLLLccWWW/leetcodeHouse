from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # 1. 分別統計兩個陣列中字串出現的頻率
        c1 = Counter(words1)
        c2 = Counter(words2)

        # 2. 統計在兩邊都恰好出現 1 次的字串數量
        ans = 0
        for word,count in c1.items():
            if count == 1 and c2[word] == 1:
                ans += 1
        return ans
