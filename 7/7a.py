import time
t0 = time.time()
invalid_ids = set()

with open("input-test.txt", "r") as f:
    inputs = f.readlines()


matrix = [input.strip() for input in inputs]
height = len(matrix)
coords = set()
def beams(grid, level, position, splits=0):
    if (level,position) in coords:
        return 0
    if level == height:
        return 0
    elif grid[level][position] in ('.','S'):
        coords.add((level,position))
        return splits + beams(grid, level+1,position)
    elif grid[level][position] == '^':
        right = 0
        left = 0
        if (position+1 < len(grid[level])):
            right = beams(grid, level,position+1)
            coords.add((level,position+1))
        if (position-1 > 0):
            left = beams(grid, level,position-1)
            coords.add((level,position-1))
    return 1+splits+right+left



print(beams(matrix, 0, matrix[0].find('S')))
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))