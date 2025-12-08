import time
t0 = time.time()

with open("inputB.txt", "r") as f:
    inputs = f.readlines()

MAX_LEVEL = 12

max_jolt = 0

def find_max(battery, level=0, start=0):
    if level == MAX_LEVEL:
        return ''
    remaining_needed = MAX_LEVEL - level
    stop = len(battery) - remaining_needed
    search_range = battery[start:stop]
    max_char = max(search_range)
    max_char_idx = battery.find(max_char, start, stop)
    next_start = max_char_idx + 1
    return max_char + find_max(battery, level+1, next_start)

for battery in inputs:
    max_battery = int(find_max(battery.strip()))
    max_jolt += max_battery

print(max_jolt)
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))