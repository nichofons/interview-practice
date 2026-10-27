class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # huh
        # okay
        # sure
        return ["." * n] + ["#" * (n-1) + "."] * (m - 1)
