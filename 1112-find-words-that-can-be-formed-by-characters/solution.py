class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)

            is_good = True
            for char,count in word_count.items():
                if chars_count[char] < count:
                    is_good = False
                    break

            if is_good:
                total_length += len(word)

        return total_length

