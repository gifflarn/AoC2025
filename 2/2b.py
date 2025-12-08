import time
t0 = time.time()
invalid_ids = set()

with open("inputB.txt", "r") as f:
    inputs = f.read()

all_ids = set()
max_id = 0

for ranges in inputs.split(','):
    start, end = ranges.split('-')
    max_val = int(end)
    if max_val > max_id:
        max_id = max_val
    for id in range(int(start), max_val+1):
        all_ids.add(id)
max_range = int(int(len(str(max_id))/2)*'9')
for i in range(max_range):
    i_str = str(i)
    check_value = i_str
    while len(check_value) <= len(str(max_id)):

        check_value+= i_str
        if int(check_value) in all_ids:
            invalid_ids.add(int(check_value))
print(sum(invalid_ids))

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))