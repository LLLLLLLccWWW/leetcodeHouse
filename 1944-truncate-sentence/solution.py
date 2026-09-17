class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 以空格分割後取前 k 個單字，再用空格合併
        return " ".join(s.split()[:k])
