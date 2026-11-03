class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # 1. 檢查長度
        if len(password) < 8:
            return False

        special_set = set("!@#$%^&*()-+")

        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        for i,ch in enumerate(password):
            # 2. 檢查相鄰是否重複
            if i > 0 and ch == password[i - 1]:
                return False

            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_set:
                has_special = True

        return has_lower and has_upper and has_digit and has_special
