class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split()
        total_spaces = text.count(' ')

        if len(words) == 1:
            return words[0] + ' ' * total_spaces

        gaps = len(words) - 1
        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        return (' ' * space_per_gap).join(words) + ' ' *  extra_spaces
