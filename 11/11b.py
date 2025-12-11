import time

t0 = time.time()

with open("input.txt", "r") as f:
    input_lines = f.readlines()

class Node:
    def __init__(self,val):
        self.val = val
        self.next_nodes = []
    
    def link(self, N):
        self.next_nodes.append(N)

    def get_paths(self):
        return self.next_nodes

    
class UniqueChain:
    def __init__(self):
        self.nodes = {} 

    def get_or_create_node(self, val):
        if val not in self.nodes:
            new_node = Node(val)
            self.nodes[val] = new_node
        return self.nodes[val]

    def link_nodes(self, val_a, val_b):
        node_a = self.get_or_create_node(val_a)
        node_b = self.get_or_create_node(val_b)
        
        node_a.link(node_b)

UC = UniqueChain()
start_node = None
for input_row in input_lines:
    source, paths = input_row.strip().split(":")
    source_node = UC.get_or_create_node(source)
    if source == "svr":
        start_node = source_node
    [UC.link_nodes(source, path) for path in paths.split()]

solved_nodes = dict()

def solve(start_node, chain):
    def dfs(node_val, have_fft, have_dac):
        input_data = (node_val, have_fft, have_dac)
        if input_data in solved_nodes:
            return solved_nodes[input_data]
        if node_val == "fft":
            have_fft = True
        if node_val == "dac":
            have_dac = True
        if node_val == "out":
            return 1 if (have_fft and have_dac) else 0
        node = chain.nodes[node_val]
        total = 0
        for nxt in node.get_paths():
            total += dfs(nxt.val, have_fft, have_dac)
        solved_nodes[input_data] = total
        return total

    return dfs(start_node.val, False, False)

def traverse(current_node, visited_nodes, visited_special):
    if current_node.val == "out":
        return 1 if ("fft" in visited_special and "dac" in visited_special) else 0

    if current_node.val in visited_nodes:
        return 0

    new_visited_nodes = visited_nodes | {current_node.val}

    new_visited_special = set(visited_special)
    if current_node.val in ("fft", "dac"):
        new_visited_special.add(current_node.val)

    total = 0
    for nxt in current_node.get_paths():
        total += traverse(nxt, new_visited_nodes, new_visited_special)

    return total
    
print(solve(start_node, UC))

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))