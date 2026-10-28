class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            # 1. 按步長 k 切片分塊
            chunks = [s[i:i + k] for i in range(0,len(s),k)]
            # 2. 計算每個分塊的 digit sum，並拼接成新字串
            s = "".join(str(sum(int(ch) for ch in chunk)) for chunk in chunks)
            
        return s
