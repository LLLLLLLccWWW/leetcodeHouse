class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # 先把第一個字串當作「目前的共同前綴」，之後再慢慢縮短。
        prefix = strs[0]
        for string in strs[1:]: # 從第二個字串開始比對
            # 逐一拿每個字串來跟 prefix 比對。
            while string.find(prefix) != 0:
                prefix = prefix[:-1]    ## 把 prefix 最後一個字元砍掉
                if not prefix:
                    return ""
        return prefix
        
