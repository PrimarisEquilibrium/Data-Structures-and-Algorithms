from collections import deque

def islandPerimeter(island):
    perimeter = [0]
    row, col = len(island), len(island[0])

    for r in range(row):
        for c in range(col):
            if island[r][c] == 1:
                start = (r, c)
                break
        else: continue
        break
    else:
        return None

    q = deque()
    q.append((start[0], start[1]))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = set()

    while q:
        row, col = q.popleft()
        visited.add((row, col))
        for dr, dc in directions:
            r, c = row + dr, col + dc

            if (r<0 or r>=row or c<0 or c>=col):                # If searched area is out of bounds
                perimeter[0] += 1
            elif island[r][c] == 0:                             # If searched area is water
                perimeter[0] += 1
            elif (island[r][c] == 1 and (r, c) not in visited): # If searched area is an island and hasn't been visited
                visited.add((r, c)) # Add it to the visited list
                q.append((r, c))    # Append it to the queue
    
    return perimeter[0]

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(islandPerimeter(grid))