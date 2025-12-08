import time
t0 = time.time()

with open("input.txt", "r") as f:
    inputs = f.readlines()



grid = []
for row in inputs:
    grid.append(row.strip())

def is_accessible(grid, x_pos, y_pos):
    if grid[y_pos][x_pos] == ".":
        return False
    rolls_of_paper = 0
    height = len(grid)
    width = len(grid[0])
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),          (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

    for dx, dy in directions:
        new_x = x_pos + dx
        new_y = y_pos + dy
        is_in_bounds = (0 <= new_x < width) and (0 <= new_y < height)
        if is_in_bounds:
            if grid[new_y][new_x] == "@":
                rolls_of_paper += 1
    return rolls_of_paper < 4

accessible_rolls = 0

for y,row in enumerate(grid):
    for x,pos in enumerate(row):
        accessible_rolls += 1 if is_accessible(grid, x, y) else 0

print(accessible_rolls)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))