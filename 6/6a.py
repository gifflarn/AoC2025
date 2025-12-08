import time
t0 = time.time()
import math
import numpy as np

with open("input.txt", "r") as f:
    inputs = f.readlines()

operations = inputs[-1].split()
numbers = [inp.strip() for inp in inputs[:-1]]
numbers = [row.split() for row in numbers]

matrix = np.array(numbers, dtype=int)
total = 0
for i,operation in enumerate(operations):
    if operation == '*':
        total += math.prod(matrix[:,i])
    elif operation == '+':
        total += sum(matrix[:,i])
print(total)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))