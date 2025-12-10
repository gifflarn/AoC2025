import time
from itertools import chain, combinations_with_replacement
t0 = time.time()
invalid_ids = set()

with open("input.txt", "r") as f:
    inputlines = f.readlines()

goal_arr = []
input_arr = []
for line in inputlines:
    row_input = []
    for i,chunk in enumerate(reversed(line.split())):
        if i == 0:
            goal_input = []
            chunks = chunk.strip('}').strip('{')
            for chr in chunks.split(","):
                goal_input.append(int(chr))
            goal_arr.append(goal_input)
        else:
            input_input = [0]*len(goal_input)
            for chr in chunk:
                if chr == '[':
                    break
                if chr in ('(',')',','):
                    continue
                input_input[int(chr)] = 1
            if any(input_input):
                row_input.append(input_input)
    input_arr.append(row_input)


def sum_to_n(n, k):
    num_splits = k - 1

    mid_with_zero = list(range(0, n + 1)) 
    splits = combinations_with_replacement(mid_with_zero, num_splits)
    for s in splits:
        cumulative_sums = list(chain([0], s, [n]))
        parts = [cumulative_sums[j] - cumulative_sums[j-1] 
                 for j in range(1, len(cumulative_sums))]
        
        yield parts

sum_calculations = 0
L = 2
complete_rows = []
while len(goal_arr) > len(complete_rows):
    for i,(goal, input) in enumerate(zip(goal_arr, input_arr)):
        if i in complete_rows: 
            continue
        for factors in sum_to_n(L,len(input)):
            result = [0]*len(goal)
            for n, input_row in zip(factors, input):
                skip = False
                for idx, val in enumerate(input_row):
                    if val == 1:
                        result[idx] += n
                    if result[idx] > goal[idx]:
                        skip = True
                if skip:
                    continue
            if result == goal:
                sum_calculations += L
                complete_rows.append(i)
                print(len(complete_rows))
                break
    L+=1
print(sum_calculations)


t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))