class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.buckets(nums, target)

    def nsquared(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
                
    def buckets(self, nums, target):
        needed = {}

        for i in range(len(nums)):
            try:
                return [needed[nums[i]], i]
            except KeyError:
                needed[target - nums[i]] = i
