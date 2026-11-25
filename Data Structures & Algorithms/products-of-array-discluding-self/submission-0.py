class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_without_zero = 1
        num_map = {}
        zero_counter = 0

        final_list = []

        for index, num in enumerate(nums):
            if num != 0:
                total_without_zero = (total_without_zero * num)
            else:
                zero_counter += 1

            total = (total * num)
            num_map[index] = num

        i = 0
        while i < len(nums):

            if zero_counter > 1:
                final_list.append(0)

            elif nums[i] == 0:
                final_list.append(round(total_without_zero / 1))
            
            else:
                final_list.append(round(total / num_map[i]))
            i += 1
        
        return final_list


            

        