class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # 單詞數量即為空格數 + 1
        return max(s.count(' ') + 1 for s in sentences)
