class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        n = len(word)

        # 列舉起點 i
        for i in range(n):
            seen = set()
            # 從起點 i 開始向右擴展
            for j in range(i,n):
                if word[j] not in vowels:
                    # 遇到非母音直接中斷，因為連續性被破壞
                    break
                seen.add(word[j])
                # 若 5 個母音皆包含，則為合法母音子字串
                if len(seen) == 5:
                    ans += 1

        return ans
