class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def word_in_int(word):
            num = 0
            for char in word:
                num = num * 10 + (ord(char) - ord('a'))
            return num

        return word_in_int(firstWord) + word_in_int(secondWord) == word_in_int(targetWord)

