import time
t0 = time.time()
invalid_ids = set()

with open("inputB.txt", "r") as f:
    inputs = f.read()

all_ids = set()
max_id = 0

for ranges in inputs.split(','):
    start, end = ranges.split('-')
    max_val = int(end)+1
    if max_val > max_id:
        max_id = max_val
    for id in range(int(start), max_val):
        all_ids.add(id)

for i in all_ids:
    i_str = str(i)
    half_i = int(len(i_str) / 2)
    if i_str[:half_i] == i_str[half_i:]:
        invalid_ids.add(i)

print(sum(invalid_ids))
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))