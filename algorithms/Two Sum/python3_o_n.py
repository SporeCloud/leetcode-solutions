class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in previous:
                return (previous[difference],i)
            else:
                previous[nums[i]] = i
