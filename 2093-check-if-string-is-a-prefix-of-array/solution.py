class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        prefix = ""

        for word in words:
            prefix += word

            # 若拼接結果恰好等於 s
            if prefix == s:
                return True

            # 剪枝：長度超出 s 時不可能再匹配
            if len(prefix) > len(s):
                return False

        return False 

