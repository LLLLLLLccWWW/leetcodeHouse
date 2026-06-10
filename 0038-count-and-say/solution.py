class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'

        for _ in range(n - 1):
            new_result = ''
            i = 0
            while i < len(result):
                char = result[i]
                count = 1
                while i + count < len(result) and result[i + count] == char:
                    count += 1
                new_result += str(count) + char
                i += count
            result = new_result

        return result
