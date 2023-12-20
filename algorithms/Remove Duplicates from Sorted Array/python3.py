class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tbr = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[tbr] = nums[i]
                tbr+=1
        return tbr
