class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = {}

        for digit in nums:
            if digit not in num_map:
                num_map[digit] = 1
            else:
                num_map[digit] += 1
        
        sorted_map = sorted(num_map, key=num_map.get, reverse=True) #give sorted num_map based on the values but descending
        return sorted_map[:k]
        