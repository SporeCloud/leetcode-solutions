class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tbr = 0
        for item in nums:
            if item != val:
                nums[tbr] = item
                tbr+=1
        
        return tbr
