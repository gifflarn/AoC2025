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
result = 0
minimum = 0
for start,end in sorted_ids:
    minimum = max(minimum, start)
    if minimum <= end:
        result += end + 1 - minimum
        minimum = end + 1
print(result)

t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))
