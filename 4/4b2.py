import time
import numpy as np

t0 = time.time()

# 1. Parse Input
# We read the file and convert it directly into a boolean NumPy array (1 for '@', 0 for others)
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

# Convert list of strings to a 2D numpy array of integers (1 or 0)
# dtype=np.uint8 is used to save memory and speed up processing
grid = np.array([[1 if c == '@' else 0 for c in row] for row in lines], dtype=np.uint8)

removed_rolls = 0

while True:
    # 2. The "Shift" Method (Colleague's suggestion)
    # To count neighbors without a slow loop, we create 8 "views" of the grid,
    # each shifted in one of the 8 directions.
    
    # Pad the grid with 0s so we can shift without losing edge data
    # padded shape becomes (H+2, W+2)
    padded = np.pad(grid, 1, mode='constant', constant_values=0)
    
    # We sum up the slices. 
    # padded[:-2, :-2] represents looking at the top-left neighbor for every cell, etc.
    neighbors = (
        padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +  # Top row
        padded[1:-1, :-2]                    + padded[1:-1, 2:] +  # Middle row (left & right)
        padded[2:, :-2]  + padded[2:, 1:-1]  + padded[2:, 2:]     # Bottom row
    )
    
    # 3. Identify items to remove
    # Logic: It must be a roll of paper (grid == 1) AND have < 4 neighbors
    to_remove_mask = (grid == 1) & (neighbors < 4)
    
    count = np.sum(to_remove_mask)
    
    # If nothing needs to be removed, the cascade is finished
    if count == 0:
        break
        
    removed_rolls += count
    
    # 4. Update the grid
    # Set the identified cells to 0 (False)
    grid[to_remove_mask] = 0

print(removed_rolls)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))