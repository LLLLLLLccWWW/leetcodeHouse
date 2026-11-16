class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = (
            length >= 10_000
            or width >= 10_000
            or height >= 10_000
            or length * width * height >= 1_000_000_000
        )
        is_heavy = mass >= 100

        if is_bulky and is_heavy:
            return "Both"
        if is_bulky:
            return "Bulky"
        if is_heavy:
            return "Heavy"
        return "Neither"
