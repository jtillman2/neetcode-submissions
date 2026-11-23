class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = {}
        for num in nums:
            if num not in numHash:
                numHash[num] = 1
            else:
                return True
        return False

        