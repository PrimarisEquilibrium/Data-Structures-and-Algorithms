from collections import deque

def island_perimeter(island):
    perimeter = [0] # Prevents referenced before assignment

    rows, cols = len(island), len(island[0]) # Gets length and columns of the grid
    visited = set() # Visited check (set)

    def bfs(r, c): # BFS Function, contains all the checks/search + expand operations
        q = deque()
        visited.add((r, c)) # Adds the current row and column to the visited check
        q.append((r, c)) # Adds the current row and column to the queue

        while q:
            row, col = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Up, down, right, left

            for dr, dc in directions:
                r, c = row + dr, col + dc # New row/column

                if (r<0 or r>=rows or c<0 or c>=cols):              # If searched area is out of bounds
                    perimeter[0] += 1
                elif island[r][c] == 0:                             # If searched area is water
                    perimeter[0] += 1
                elif (island[r][c] == 1 and (r, c) not in visited): # If searched area is an island and hasn't been visited
                    visited.add((r, c)) # Add it to the visited list
                    q.append((r, c))    # Append it to the queue

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited: # Looks for the first island block that hasn't been visited
                bfs(r, c)                                 # Runs the BFS function
                return perimeter[0]                       # Returns the perimeter

grid = [[0,1,0,0]]
print(island_perimeter(grid))