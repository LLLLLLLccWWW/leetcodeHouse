class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        # 統計以 pref 開頭的字串數量
        return sum(1 for word in words if word.startswith(pref))
