import operator
dial_val = 50
pwd = 0

with open("inputA.txt", "r") as f:
    inputs = f.readlines()

for line in inputs:
    if line[0] == "R":
        op = operator.add
    else:
        op = operator.sub
    dial_val = op(dial_val, int(line[1:])) % 100
    if dial_val == 0:
        pwd += 1
print(pwd)
