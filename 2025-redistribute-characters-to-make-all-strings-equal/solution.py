from collections import Counter
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)

        # 統計所有字串中每個字母出現的總次數
        char_counts = Counter("".join(words))

        # 檢查每個字母的總次數是否都能被 n 整除
        return all(count % n == 0 for count in char_counts.values())
