class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        def digit_sum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        group_count = {}
        for i in range(1,n + 1):
            key = digit_sum(i)
            group_count[key] = group_count.get(key,0) + 1

        max_size = max(group_count.values())
        return sum(1 for size in group_count.values() if size == max_size)
