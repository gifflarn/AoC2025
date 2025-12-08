import time
t0 = time.time()
import operator
dial_val = 50
pwd = 0

with open("inputB.txt", "r") as f:
    inputs = f.readlines()

for line in inputs:
    direction = line[0]
    rotation = int(line[1:])
    op = operator.add if direction == "R" else operator.sub
    pre_dial = dial_val
    pre_dial = pre_dial % 100
    pwd += rotation // 100
    dial_val = op(dial_val, rotation)
    if pre_dial and (direction == "R" and dial_val >= 100 or direction == "L" and dial_val <= 0):
        pwd += 1
    dial_val = dial_val % 100
print(pwd)
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))