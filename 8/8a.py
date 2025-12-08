import time
t0 = time.time()
invalid_ids = set()

with open("input.txt", "r") as f:
    inputs = f.readlines()


matrix = [[int(k) for k in j.strip().split(",")] for j in inputs]

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)
        self.parent[x_rep] = y_rep


def kruskals_mst(V, edges):

    edges = sorted(edges,key=lambda x:x[2])
    
    dsu = DSU(V)
    for x, y, w in edges[:1000]:
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
    return dsu

all_edges = set()
V = len(matrix)


for i in range(V):
    for j in range(i + 1, V):
        p1 = matrix[i]
        p2 = matrix[j]
        weight = (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2
        all_edges.add((i, j, weight))

final_edges = list(all_edges)
final_dsu = kruskals_mst(len(matrix), final_edges)
V = len(matrix)
circuit_sizes = {}

for i in range(V):
    root = final_dsu.find(i)
    circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

sizes = sorted(circuit_sizes.values(), reverse=True)
mult = 1
print(sizes)
for s in sizes[:3]:
    mult *= s
print(mult)


t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))