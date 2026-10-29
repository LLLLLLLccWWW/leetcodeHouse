class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res =[words[0]]

        for i in range(1,len(words)):
            # 只有當當前字詞與 res 中最新保留的字詞不是 Anagram 時才加入
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])

        return res
