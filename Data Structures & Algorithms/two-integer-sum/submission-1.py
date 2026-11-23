class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement not in num_map:
                num_map[nums[index]] = index
            else:
                return [num_map[complement]] + [index]
        
        