class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        for i in range(0,len(s),k):
            chunk = s[i:i + k]
            # 若長度不足 k，用 fill 字元向右補足至長度 k
            res.append(chunk.ljust(k,fill))
        return res
