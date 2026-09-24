class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        covered = [False] * 52

        # 標記被區間覆蓋到的所有數字
        for start,end in ranges:
            for x in range(start, end + 1):
                covered[x] = True

        # 檢查 [left, right] 範圍內是否每個數字都被覆蓋
        return all(covered[x] for x in range(left, right + 1))
