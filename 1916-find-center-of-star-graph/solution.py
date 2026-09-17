class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # 只要比較前兩條邊: edges[0] = [u1, v1], edges[1] = [u2, v2]
        # 如果 edges[0][0] 出現在 edges[1] 中，它就是中心點，否則 edges[0][1] 是中心點
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
