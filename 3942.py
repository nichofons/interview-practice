class Solution:
    def minOperations(self, nums: List[int]) -> int:
        change = [1, -1]
        zero_loc = nums.index(0)

        if len(nums) == 1:
            return 0
        


        for rel_index in range(1, len(nums)):
            val = nums[(rel_index + zero_loc) % len(nums)]

            if val != rel_index:
                change[0] = 0
            if val != len(nums) - rel_index:
                change[1] = 0
            
            if change[0] == 0 and change[1] == 0:
                return -1
        
        if change[0]:
            return min(zero_loc, len(nums) - zero_loc + 2)

        return min(len(nums) - zero_loc, zero_loc +2)
        
