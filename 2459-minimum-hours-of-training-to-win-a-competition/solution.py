class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        training_hours = 0

        # 1. 計算精力所需的補充小時數
        total_required_energy = sum(energy) + 1
        if initialEnergy < total_required_energy:
            training_hours += total_required_energy - initialEnergy

        # 2. 模擬經驗值的補充
        curr_exp = initialExperience
        for exp in experience:
            if curr_exp <= exp:
                diff = exp - curr_exp + 1
                training_hours += diff
                curr_exp += diff
            curr_exp += exp

        return training_hours
        
