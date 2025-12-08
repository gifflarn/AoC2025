import time
import copy
t0 = time.time()
invalid_ids = set()

with open("input.txt", "r") as f:
    inputs = f.readlines()

id_ranges = set()
fresh_ingredients = 0
ranges = True

def get_ids(input):
    start, end = input.split("-")
    id_ranges.add((int(start),(int(end))))


for input in inputs:
    if not (input := input.strip()):
        break
    if '-' in (input):
        get_ids(input)

sorted_ids = list(id_ranges)
sorted_ids = sorted(sorted_ids, key= lambda x: x[0])
i = 0
while i < len(sorted_ids) - 1:
    current_range = sorted_ids[i]
    next_range = sorted_ids[i+1]
    old_sorted = copy.deepcopy(sorted_ids)
    if current_range[1] >= next_range[0]:
        new_start = current_range[0]
        new_end = max(current_range[1], next_range[1])
        sorted_ids[i] = (new_start, new_end)
        del sorted_ids[i+1]
    else:
        i = i+1
print(sorted_ids)
total = 0
for start,end in sorted_ids:
    print(start, '-', end)
    total+= (end-start+1)
print(total)

t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))
