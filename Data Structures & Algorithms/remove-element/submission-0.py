class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        flag=0
        res=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                flag+=1
                res.append(nums[i])
        nums[:]=res
        return flag