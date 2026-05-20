class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)     # 字串轉list才能修改
        for i in range(0, len(s), 2*k):  # 每次跳 2k
            s[i:i+k] = s[i:i+k][::-1]   # 反轉前k個

        return ''.join(s)
