class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num_map = {}
        for digit in nums:
            if digit in num_map:
                return True
            else:
                num_map[digit] = 1
        
        return False