class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        return self.checkAll(grid)

    def checkAll(self, grid: list[list[int]]) -> int:
        """
        just check every path
        """
        try:
            return self.dfs(grid, 0, 0, 1024, 0)
        except:
            return 0
    
    def dfs(self, grid, x, y, min_val, val):
        m = len(grid)
        n = len(grid[0])
        new_val = val ^ grid[x][y]

        if x < m - 1:
            min_val = self.dfs(grid, x + 1, y, min_val, new_val)
        if y < n - 1:
            min_val = self.dfs(grid, x, y + 1, min_val, new_val)
        if (x == m - 1 and y == n - 1):
            if new_val < min_val:
                min_val = new_val
                if min_val == 0:
                    raise Exception
        return min_val
