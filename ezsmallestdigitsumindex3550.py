# You are given an integer array nums.

# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

# If no such index exists, return -1.


# I don't like how i calculated the sum, maybe there's a better way
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if nums[index] % 10 + (nums[index] % 100) // 10 + (nums[index] % 1000) // 100 + (nums[index] == 1000) == index:
                return nums[index] % 10 + (nums[index] % 100) // 10 + (nums[index] % 1000) // 100 + (nums[index] == 1000)
        return -1
