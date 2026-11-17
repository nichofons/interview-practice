# halffinished whoops

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        up_seq = 1
        cur_seq = 1
        asc = None

        for i in range(1, len(nums):
            if nums[i] > nums[i - 1]:

            if asc == None:
                if i > last:
                    asc = True
                
            if (i > last and asc == True) or (i < last and asc == False):
                cur_seq += 1
            else:
                if (cur_seq > most_seq):
                    most_seq = cur_seq
                cur_seq = 1
                asc = not asc
            last = i
        
        return most_seq
