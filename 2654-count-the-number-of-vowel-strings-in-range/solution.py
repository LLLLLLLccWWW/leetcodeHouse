class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return sum(
            words[i][0] in vowels and words[i][-1] in vowels
            for i in range(left,right + 1)       
        )
