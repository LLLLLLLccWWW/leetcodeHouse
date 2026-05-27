class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        child = 0  # 孩子指標
        cookie = 0  # 餅乾指標

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:  # 餅乾夠大
                child += 1             # 這個孩子滿足了
            cookie += 1                # 不管有沒有滿足，餅乾都用掉

        return child
