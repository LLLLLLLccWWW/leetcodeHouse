class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(d) for d in str(n)]   # 把每個位數取出來

        product = 1
        for d in digits:
            product *= d

        return product - sum(digits)
