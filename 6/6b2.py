import time
t0 = time.time()
import math

with open("input-test.txt", "r") as f:
    inputs = f.readlines()

numbers = inputs[:-1]
operations_raw = inputs[-1]
operations = []
column_width = []
col_width = 0
for char in operations_raw:
    if char in ('*','+'):
        if col_width:
            column_width.append(col_width-1)
        operations.append(char)
    col_width += 1
column_width.append(col_width)


data = []
for number in numbers:
    number = number.strip("\n")
    number_arr = []
    whole_nbr = ""
    col_ctr = 0
    for i,n in enumerate(number):
        whole_nbr += n
        if i == column_width[col_ctr]:
            col_ctr +=1
            number_arr.append(whole_nbr[:-1])
            whole_nbr = ""
        if i == len(number)-1:
            number_arr.append(whole_nbr)

    data.append(number_arr)

total = 0
for i,operation in enumerate(operations):
    height = len(data)
    slice = [data[k][i] for k in range(height)]
    new_numbers = ['']*(height)
    for num in slice:
        for j,n in enumerate(num):
            try:
                int(n)
            except:
                n = ' '
            new_numbers[j] += n
    print(new_numbers)
    int_values = []
    for num in new_numbers:
        if not ''.join(num).strip():
            continue
        int_values.append(int(''.join(num).strip()))
    if operation == '*':
        total += math.prod(int_values)
    elif operation == '+':
        total += sum(int_values)
print(total)
t1 = time.time()
print("executed in {0:0.9f}ms".format((t1-t0)*1000))