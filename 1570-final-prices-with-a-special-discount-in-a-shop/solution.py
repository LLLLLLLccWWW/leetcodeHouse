class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        result = prices[:]
        stack = []  # 存 index，單調遞增堆疊

        for i in range(len(prices)):
            # 當前價格 <= stack頂端的價格，找到折扣了！
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] -= prices[i]
            stack.append(i)
        return result

        
