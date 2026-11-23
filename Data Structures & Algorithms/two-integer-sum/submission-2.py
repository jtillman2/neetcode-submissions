class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}
        index = 0
        for digit in nums:

            if (target - digit) in num_map:
                return [num_map[(target-digit)], index]
            else:
                num_map[digit] = index # {4:0, 6:1, 8:2}
                index += 1

        

        