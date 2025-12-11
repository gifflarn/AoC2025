import time
import pulp

t0 = time.time()

goal_arr = []
input_arr = []

with open("input.txt", "r") as f:
    inputlines = f.readlines()


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

total_sum = 0

for i, (goal, inputs) in enumerate(zip(goal_arr, input_arr)):
    n = len(inputs)

    prob = pulp.LpProblem(str(i), pulp.LpMinimize)
    pulps = []
    for j in range(n):
        variable = pulp.LpVariable(f"x{j}", lowBound=0, cat='Integer')
        pulps.append(variable)
    for col in range(len(goal)):
        column_sum = 0
        for row in range(n):
            column_sum += pulps[row] * inputs[row][col]
        prob += column_sum == goal[col]
    prob += pulp.lpSum(pulps)

    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
    solution = [int(pulp.value(var)) for var in x]
    row_sum = sum(solution)
    total_sum += row_sum

print(total_sum)
t1 = time.time()
print(f"Executed in {(t1-t0)*1000:0.1f}ms")