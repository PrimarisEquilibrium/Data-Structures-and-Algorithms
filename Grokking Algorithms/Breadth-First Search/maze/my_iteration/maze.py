from collections import deque

def solve_maze(maze):
    R, C = len(maze), len(maze[0])
    start = (0, 0)

    for r in range(R):
        for c in range(C):
            if maze[r][c] == "S":
                start = (r, c)
                break
        else: continue
        break
    else:
        return None
    
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = set()

    while len(queue) != 0:
        coord = queue.pop()
        visited.add((coord[0], coord[1]))

        if maze[coord[0]][coord[1]] == "E":
            return coord[2]
        
        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or (nr, nc) in visited): continue
            queue.appendleft((nr, nc, coord[2] + 1))

with open("Grokking Algorithms\Breadth-First Search\maze\my_iteration\maze.txt") as f:
    maze = []
    for line in f:
        maze.append([i for i in line.strip("\n")])
    print(solve_maze(maze))