from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
        res = -1
        for num,freq in count.items():
            if num == freq:
                res = max(res,num)
        return res
