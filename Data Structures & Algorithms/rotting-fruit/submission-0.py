class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0, -1]]
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        def rot_neighbor(r,c):
            infected = 0

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<= nr < rows and
                    0<= nc < cols and
                    grid[nr][nc] == 1):

                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    infected += 1

            return infected

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                fresh -= rot_neighbor(r,c)
            minutes += 1

        return minutes if fresh == 0 else -1
