from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        count = Counter(s1.split() + s2.split())
        
        # 篩選出出現次數恰好為 1 的單字
        return [word for word,freq in count.items() if freq == 1]

