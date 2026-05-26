class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set(path[0] for path in paths)    # 所有起點

        for path in paths:
            if path[1] not in sources:  # 終點不是任何路線的起點
                return path[1]
