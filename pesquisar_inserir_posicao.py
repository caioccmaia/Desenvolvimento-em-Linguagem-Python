class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] ==  target - 1:
                return (i+1)
