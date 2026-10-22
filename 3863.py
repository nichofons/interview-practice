# solved with heavy hints
# https://www.youtube.com/watch?v=xTQVW3KMkpE

class Solution:
    def minOperations(self, s: str) -> int:

        last = '0'
        for i in s:
            if ord(last) > ord(i):
                last = -1
                break
            last = i
        
        if last != -1:
            return 0
        if len(s) == 2: return -1


        maxc = max(s)
        minc = min(s)
        if s[0] == minc or s[-1] == maxc:
            return 1

        for i in s[1:-1]:
            if i == maxc or i == minc:
                return 2
    
        return 3
