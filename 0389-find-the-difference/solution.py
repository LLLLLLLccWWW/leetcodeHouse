from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = Counter(t) - Counter(s)  # t的字母數 - s的字母數
        return list(count.keys())[0]     # 剩下的就是多的那個

