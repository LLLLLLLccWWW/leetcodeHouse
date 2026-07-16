class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        num_rows = len(strs)
        num_cols = len(strs[0])

        delete_count = 0

        for col in range(num_cols):
            for row in range(num_rows - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete_count += 1
                    break

        return delete_count
