import time
t0 = time.time()
from collections import deque

with open("input.txt", "r") as f:
    inputs = f.readlines()

grid = []
for row in inputs:
    grid.append([c == "@" for c in list(row.strip())])


MAX_HEIGHT = len(grid)
MAX_WIDTH = len(grid[0])
queue = deque()
accessible_coords = set()

removed_rolls = 0
directions = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),          (1, 0),
    (-1, 1), (0, 1), (1, 1)
]
for y,row in enumerate(grid):
    for x in range(len(row)):
        if not grid[y][x]:
            continue
        rolls_of_paper = 0

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < MAX_WIDTH) and (0 <= new_y < MAX_HEIGHT) and grid[new_y][new_x]:
                rolls_of_paper += 1
        if rolls_of_paper < 4:
            removed_rolls += 1
            queue.append((y, x))
            accessible_coords.add((y, x))
            grid[y][x] = False
while queue:
    cy, cx = queue.pop()
    grid[cy][cx] = False
    
    for dx, dy in directions:
        ny, nx = cy + dy, cx + dx
        if (0 <= nx < MAX_WIDTH) and (0 <= ny < MAX_HEIGHT) and (ny, nx) not in accessible_coords:
            if grid[ny][nx]:
                rolls_of_paper = 0
                for ndx, ndy in directions:
                    nnx, nny = nx + ndx, ny + ndy
                    if (0 <= nnx < MAX_WIDTH) and (0 <= nny < MAX_HEIGHT) and grid[nny][nnx]:
                        rolls_of_paper += 1
                
                if rolls_of_paper < 4:
                    removed_rolls += 1
                    queue.append((ny, nx))
                    accessible_coords.add((ny, nx))
                    grid[ny][nx] = False

print(removed_rolls)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))