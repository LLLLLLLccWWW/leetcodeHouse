class Solution:
    def oddString(self, words: list[str]) -> str:
        # 輔助函式：計算字串的差值 tuple
        def get_diff(word:str) -> tuple[int,...]:
            return tuple(ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))

        d0 = get_diff(words[0])
        d1 = get_diff(words[1])

        # 前兩個相同，主流為 d0，從第 3 個開始比對
        if d0 == d1:
            for i in range(2,len(words)):
                if get_diff(words[i]) != d0:
                    return words[i]

        # 前兩個不同，透過第 3 個 (d2) 判斷異類為 words[0] 或 words[1]
        d2 = get_diff(words[2])
        return words[1] if d0 == d2 else words[0]
