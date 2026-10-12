class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # find trasures
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        # bfs for different directions with calculations
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (
                    0<= nr < rows and
                    0<= nc < cols and
                    grid[nr][nc] == INF
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

