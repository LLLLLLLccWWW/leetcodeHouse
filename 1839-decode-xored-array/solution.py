class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]

        for num in encoded:
            # arr 的最後一個元素與 encoded[i] 進行 XOR，得出下一個數字
            arr.append(arr[-1] ^ num)

        return arr
