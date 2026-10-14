from collections import Counter
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1,c2 = Counter(word1),Counter(word2)
        # 聯集所有出現過的字母進行差值檢查
        return all(abs(c1[ch] - c2[ch]) <= 3 for ch in set(word1 + word2))
