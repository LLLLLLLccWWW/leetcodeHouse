from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # 以第一個字串的字元頻率作為基準
        common = Counter(words[0])

        # 依次與後續每個字串取交集（保留最小頻率
        for word in words[1:]:
            common &= Counter(word)

        # 將 Counter 展開回字元陣列
        return list(common.elements())
