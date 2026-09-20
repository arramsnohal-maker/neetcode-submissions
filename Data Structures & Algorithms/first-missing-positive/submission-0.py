class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        num = 1
        for i in range(len(nums)):
            if nums[i] == num:
                num+=1
            elif nums[i]>num:
                return num
        return num    