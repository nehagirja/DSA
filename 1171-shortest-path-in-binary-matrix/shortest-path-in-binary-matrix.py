class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        queue = deque([(0, 0, 1)]) 
        visited = set((0,0))
        neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        while queue:
                r, c, total = queue.popleft() 
                if r == N - 1 and c == N - 1:
                    return total

                for dr, dc in neighbours:
                    if (0 <= r + dr < N and 0 <= c + dc < N and grid[r + dr][c + dc] == 0 and (r + dr, c + dc) not in visited):                    
                        queue.append((r + dr, c + dc, total + 1))
                        visited.add((r + dr, c + dc))
        return -1