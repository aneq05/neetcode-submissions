class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_len_seen = 0

        def dfs(r,c):
            nonlocal max_len_seen
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c] == 0):
                return 0

            visited.add((r,c))
            curr_sum = 0
            for dr, dc in directions:
                curr_sum += dfs(r+dr, c+dc)
            
            return curr_sum + 1
                

        for r in range(rows):
            for c in range(cols):
                max_len_seen = max(max_len_seen, dfs(r,c))

        return max_len_seen