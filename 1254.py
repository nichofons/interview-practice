# doesnt work ill fix eventually1
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        islands = []
        closed = 0

        visited = [[0 for i in grid] for k in grid[0]]

        for x_index in range(len(grid)):
            for y_index in range(len(grid[x_index])):
                if grid[x_index][y_index] == 0 and visited[x_index][y_index] == 1 \
                    and self.dfs(x_index, y_index, grid, visit):
                    closed += 1
        
        def dfs(self, x: int, grid: List[List[int]], visit: List[List[bool]]) -> bool:
            m = len(grid)
            n = len(grid[0])
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if grid[x][y] == 1 or visit[x][y]:
                return True

            visit[x][y] = True
            is_closed = True
            dirx = [0, 1, 0, -1]
            diry = [-1, 0, 1, 0]

            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if not self.dfs(r, c, m, n, grid, visit):
                    is_closed = False

            return is_closed
