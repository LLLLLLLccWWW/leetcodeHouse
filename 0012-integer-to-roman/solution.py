class Solution(object):
    def intToRoman(self, num):
    # 從大到小列出所有對應關係（包含特殊情況）
        val_sym = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        result = ''     # 空字串，之後一個一個把羅馬符號加進來
        for val,sym in val_sym:     # 從大到小依序取出
            while num >= val:   # 只要 num 還比這個值大，就一直用
                result += sym   # 把符號加到結果
                num -= val      # num 扣掉這個值
        return result

        
