from collections import Counter
from functools import reduce
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # 手寫 輾轉相除法 (GCD)
        def gcd(a,b):
            while b:
                a,b = b, a % b
            return a

        counts = Counter(deck).values()

        g = reduce(gcd,counts)

        return g >= 2
