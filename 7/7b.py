import time
t0 = time.time()

with open("input.txt", "r") as f:
    inputs = f.readlines()

matrix = [input.strip() for input in inputs]
height = len(matrix)


coords = dict()
def parse(grid, level, position):
    if level == height - 1:
        return 1
    if level >= height or position < 0 or position >= len(grid[0]):
        return 0
    if (level, position) in coords:
        return coords[(level, position)]
    elif grid[level][position] in ('.','S'):
        return parse(grid, level+1,position)
    elif grid[level][position] == '^':
        left = parse(grid, level+1, position - 1)
        right = parse(grid, level+1, position + 1)
        paths = left + right
        coords[(level, position)] = paths
        return paths


root = parse(matrix, 0, matrix[0].find('S'))
print(root)
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))