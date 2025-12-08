import time
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
        continue
    if '-' in (input):
        get_ids(input)
    else:
        for start, end in id_ranges:
            if start <= int(input) <= end:
                fresh_ingredients+=1
                break

print(fresh_ingredients)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))
