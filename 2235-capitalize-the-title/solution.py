class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        res = []

        for w in words:
            w_lower = w.lower()
            if len(w) <= 2:
                res.append(w_lower)
            else:
                res.append(w_lower.capitalize())

        return " ".join(res)
