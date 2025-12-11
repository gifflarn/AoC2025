import time
t0 = time.time()

with open("input-test.txt", "r") as f:
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
        print(f"Linked {val_a} -> {val_b}")
    
paths = dict()
for input_row in input_lines:
    source, path = input_row.strip().split(":")
    paths[source] = path.split()


for key,values in paths.items():
    node = Node(key)
    
    for value in values:
        node.link(Node(value))




nbr_complete_paths = 0

def traverse(current_path, visited_paths):
    if current_path == "out":
        if "fft" in visited_paths and "dac" in visited_paths:
            return 1
        else:
            return 0
    next_paths = paths[current_path]
    if current_path in visited_paths:
        return 0
    visited_paths.append(current_path)
    print(visited_paths)
    return sum([traverse(p, visited_paths[:]) for p in next_paths])
    

starting_point = "svr"
print(traverse(starting_point,[]))

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))