class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS  = len(grid), len(grid[0])
        q = deque()
        fresh, minutes = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r, c, 1))

        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q and fresh > 0:
            r, c, minutes = q.popleft()
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                    continue 
            
                grid[nr][nc] = 2
                q.append((nr, nc, minutes + 1))
                fresh -= 1

        return minutes if fresh == 0 else -1