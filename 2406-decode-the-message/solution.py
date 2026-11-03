class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ':' '}
        curr_code = ord('a')

        # 1. 建立密碼表
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(curr_code)
                curr_code += 1
                if curr_code > ord('z'):
                    break

        # 2. 解密訊息
        return "".join(mapping[ch] for ch in message)
