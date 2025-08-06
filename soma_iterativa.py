class Solution:
    def twoSum(self, nums, alvo):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == alvo:
                    return [i, j]
        return None
