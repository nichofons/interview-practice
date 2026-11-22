class Solution:
    def checkString(self, s: str) -> bool:
        return self.brute(s)



    def brute(self, s):
        b = False
        for i in s:
            if b and i == "a":
                return False
            elif i == 'b' and not b:
                b = True
        return True
