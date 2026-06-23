class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_s = {}
        s_to_p = {}

        for char,word in zip(pattern,words):
            if char in p_to_s:
                if p_to_s[char] != word:
                    return False
            else:
                p_to_s[char] = word

            if word in s_to_p:
                if s_to_p[word] != char:
                    return False
            else:
                s_to_p[word] = char

        return True
