class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return self.math_solution(nums)

    def math_solution(self, nums):
        return max(nums) * len(nums) - sum(nums)

    def normal_solution(self, nums):
        last_max = 0
        moves = 0
        diff = 0

        for index in range(len(nums)):
            if last_max < nums[index]:
                diff = nums[index] - last_max 
                last_max = nums[index]
                moves += diff * index
            else:
                moves += last_max - nums[index]
        
        return moves
