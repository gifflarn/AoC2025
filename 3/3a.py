import time
t0 = time.time()

with open("inputA.txt", "r") as f:
    inputs = f.readlines()

max_jolt = 0

for battery in inputs:
    for x in list(reversed(range(10))):
        found = False
        idx = battery.find(str(x))
        if idx >= 0:
            for y in list(reversed(range(10))):
                idx2 = battery[idx+1:].find(str(y))
                if idx2 >= 0:
                    max_jolt += int(battery[idx] + battery[idx+1+idx2])
                    found = True
                    break
            if found:
                break

print(max_jolt)
t1 = time.time()
print("executed in {0:0.9f}µs".format((t1-t0)*1000000))