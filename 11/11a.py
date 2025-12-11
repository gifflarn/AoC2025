import time
t0 = time.time()

with open("input.txt", "r") as f:
    input_lines = f.readlines()


paths = dict()
for input_row in input_lines:
    source, path = input_row.strip().split(":")
    paths[source] = path.split()

nbr_complete_paths = 0

def traverse(current_path, visited_paths):
    if current_path == "out":
        return 1
    next_paths = paths[current_path]
    if current_path in visited_paths:
        return 0
    visited_paths.append(current_path)
    return sum([traverse(p, visited_paths[:]) for p in next_paths])
    

starting_point = "you"
print(traverse(starting_point,[]))

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))