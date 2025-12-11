import time

t0 = time.time()

with open("input.txt", "r") as f:
    input_lines = f.readlines()

start_node = None
graph = {}
for input_row in input_lines:
    source, paths = input_row.strip().split(":")
    graph[source] = paths.split()

solved_nodes = dict()

def traverse(node_val, have_fft, have_dac):
    input_data = (node_val, have_fft, have_dac)
    if input_data in solved_nodes:
        return solved_nodes[input_data]
    if node_val == "fft":
        have_fft = True
    if node_val == "dac":
        have_dac = True
    if node_val == "out":
        result = 1 if (have_fft and have_dac) else 0
        solved_nodes[input_data] = result
        return result
    total = 0
    for nxt in graph.get(node_val, []):
        total += traverse(nxt, have_fft, have_dac)
    solved_nodes[input_data] = total
    return total

    
print(traverse("svr", False, False))

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))