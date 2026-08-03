class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ans = []
        cur = 0

        for bit in nums:
            # 每次左移一位 (相當於 * 2) 並加上當前位元，然後對 5 取模
            cur = (cur * 2 + bit) % 5

            # 若餘數為 0，代表能被 5 整除
            ans.append(cur == 0)

        return ans
