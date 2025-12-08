import time
t0 = time.time()
import math
import numpy as np
from io import StringIO

with open("input.txt", "r") as f:
    inputs = f.readlines()

numbers = inputs[:-1]
operations_raw = inputs[-1]
operations = []
column_width = []
col_width = 0
for char in operations_raw:
    if char in ('*','+'):
        if col_width:
            column_width.append(col_width)
        operations.append(char)
        col_width = 1
    else:
        col_width += 1
column_width.append(col_width)

data = np.genfromtxt(
    StringIO(''.join(numbers)),
    delimiter=column_width,
    dtype=str,
    encoding=None,
)
total = 0
for i,operation in enumerate(operations):
    new_numbers = ['']*len(data[:,i])
    for j,num in enumerate(data[:,i]):
        for n in num:
            try:
                int(n)
            except:
                n = ' '
            new_numbers[j] += n
    new_data = np.genfromtxt(StringIO('\n'.join(new_numbers)), dtype=str, delimiter=[1]*len(new_numbers))
    int_values = []
    for j in range(len(new_numbers)):
        if not ''.join(new_data[:,j]).strip():
            continue
        int_values.append(int(''.join(new_data[:,j])))
    if operation == '*':
        total += math.prod(int_values)
    elif operation == '+':
        total += sum(int_values)
print(total)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))