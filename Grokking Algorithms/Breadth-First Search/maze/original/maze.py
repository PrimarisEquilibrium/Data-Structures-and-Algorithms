# ---------------------------------------------------------------------------- #
#                          MAZE SHORTEST PATH PROGRAM                          #
# ---------------------------------------------------------------------------- #

from collections import deque

def solveMaze(maze):

# -------------------------- Variable Initialization ------------------------- #

    R, C = len(maze), len(maze[0]) # Gathers the amount of rows and columns in the maze
    start = (0, 0)                  # Initializes a starting value

    # Loop to find out the starting point of the maze
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)
                break
        else: continue  # Break from the nested loop
        break
    else:
        return None     # If no starting point is found return None

    queue = deque() # Queue Initalization
    queue.appendleft((start[0], start[1], 0)) # Appends the coordinates of the starting value to the queue
                                              # 0 is the distance away from the starting point

                                                    # Possible directions (Not including diagonals)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # Right, Left, Down, Up
    visited = [[False] * C for _ in range(R)]       # Builds a 2D array using "False" | Avoids infinite loops

# ---------------------------------------------------------------------------- #
#                                    Summary                                   #        
#   - Get the rows/columns of the graph                                        #
#   - Create and find the starting point                                       #
#   - Create a queue (Used to store the different directions taken)            #
#   - Append the starting point to the queue                                   #
#   - Create a list of possible directions                                     #
#   - Create a list of visited locations                                       #
#       - (Either by a boolean matrix, or list/dictionary of existed values)   #
# ---------------------------------------------------------------------------- #

# -------------------- Breadth-First Search Implimentation ------------------- #

    while len(queue) != 0:                  # While there is still a path in the queue follow it, once no more paths exists: exit
        coord = queue.pop()                 # Pops the top most element from the queue (oldest)
        visited[coord[0]][coord[1]] = True  # Alters the visited coord to true (Visited)

        if maze[coord[0]][coord[1]] == "E": # Checks if we are at the end of the maze
            return coord[2]                 # Returns the amount of steps it took to make it the end
        
        # Checks for all possible locations we can move to
        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1] # NR/NC = New Row/Column
            if (nr < 0 or nr >= R or nc < 0 or nc > C or maze[nr][nc] == "#" or visited[nr][nc]): continue # Don't visit
                # Checks if true:
                #   - NR (New row) is out of bounds, less than 0 | Greater or equal to out bounds of the maze
                #   - NC (New column) is out of bounds
                #   - The position we are moving towards is a wall
                #   - If we have already visited the location
            queue.appendleft((nr, nc, coord[2] + 1))

# ---------------------------------------------------------------------------- #
#                                    Summary                                   #
#   - While loop runs until the search space is cleared                        #
#   - Grab the most recent coordinates and add a visiting status               #
#   - Check for the base case, or the end result                               #
#   - If end result is not met append the other valid directions to the queue  #
# ---------------------------------------------------------------------------- #

# --------------------------- File Opening / Output -------------------------- #

with open("maze.txt") as f:                         # Opens the file
    maze = []                                       
    for line in f:                                  # Loops through each line the the file
        maze.append([i for i in line.strip("\n")])  # Adding that line by spliting the line it its own seperate list
                                                    # Removes any new line characters
    print(solveMaze(maze))