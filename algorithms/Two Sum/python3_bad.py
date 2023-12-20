class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        products = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i]+nums[j]
                products[product] = (i,j)
        
        return products[target]
