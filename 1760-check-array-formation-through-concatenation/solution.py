class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        piece_map = {piece[0]: piece for piece in pieces}

        i = 0
        n = len(arr)

        while i < n:
            if arr[i] not in piece_map:
                return False

            piece = piece_map[arr[i]]
            for num in piece:
                if i>=n or arr[i] != num:
                    return False
                i += 1

        return True
