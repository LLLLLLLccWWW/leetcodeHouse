class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary)
        total -= max(salary)
        total -= min(salary)
        return float(total) / (len(salary) - 2)
