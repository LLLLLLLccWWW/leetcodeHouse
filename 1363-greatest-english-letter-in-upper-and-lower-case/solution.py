class Solution:
    def greatestLetter(self, s: str) -> str:
        char_set = set(s)

        # 從 'Z' 倒數至 'A' (ord('Z') = 90, ord('A') = 65)
        for code in range(ord('Z'), ord('A') - 1, -1):
            ch = chr(code)
            # 同時存在大寫與小寫
            if ch in char_set and ch.lower() in char_set:
                return ch

        return ""
