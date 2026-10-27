class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # the numbah of islands to return
        numbah = 0

        # size of the grid
        m = len(grid)
        n = len(grid[0])

        # visited grid
        visited = [[0 for i in range(n)] for k in range(m)]

        # traverse
        for x in range(m):
            for y in range(n):
                if visited[x][y] == 1:
                    continue
                if grid[x][y] == 0:
                    visited[x][y] = 1
                    continue
                island_sum = self.dfs(grid, x, y, visited, 0)
                if island_sum % k == 0:
                    numbah += 1
        return numbah


    def dfs(self, grid, x: int, y: int, visited: List[List[int]], island_sum: int):

        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]):
            return island_sum
        if visited[x][y]:
            return island_sum
        visited[x][y] = 1
        if grid[x][y] == 0:
            return island_sum
        island_sum += grid[x][y]

        directions = [[-1,0], [1,0], [0,-1], [0, 1]]

        for adir in directions:
            island_sum += self.dfs(grid, x + adir[0], y + adir[1], visited, 0)


        return island_sum
        
