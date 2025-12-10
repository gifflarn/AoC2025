import time
import itertools
t0 = time.time()
invalid_ids = set()

with open("input.txt", "r") as f:
    inputlines = f.readlines()

goal_arr = []
input_arr = []
for line in inputlines:
    row_input = []
    for i,chunk in enumerate(line.split()):
        if i == 0:
            goal_input = []
            for chr in chunk:
                if chr == '.':
                    goal_input.append(0)
                elif chr in ('[',']'):
                    continue
                else:
                    goal_input.append(1)
            goal_arr.append(goal_input)
        else:
            input_input = [0]*len(goal_input)
            for chr in chunk:
                if chr == '{':
                    break
                if chr in ('(',')',','):
                    continue
                input_input[int(chr)] = 1
            if any(input_input):
                row_input.append(input_input)
    input_arr.append(row_input)

sum_calculations = 0
L = 1
complete_rows = []
while len(goal_arr) > len(complete_rows):
    for i,(goal, input) in enumerate(zip(goal_arr, input_arr)):
        if i in complete_rows: 
            continue
        for subsets in itertools.combinations(input, L):
            result = [0]*len(subsets[0])
            for s in subsets:
                result = [(a+b)%2 for a, b in zip(s, result)]
            if result == goal:
                sum_calculations += L
                complete_rows.append(i)
                break
    L+=1
print(sum_calculations)


t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))