class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0

        # 當 word 重複 k + 1 次依然是 sequence 的子字串時，繼續累加
        while (word * (k + 1)) in sequence:
            k += 1
        return k
