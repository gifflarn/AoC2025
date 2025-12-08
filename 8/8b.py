import time
t0 = time.time()
invalid_ids = set()

with open("input-test.txt", "r") as f:
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
        if x_rep != y_rep:
            self.parent[x_rep] = y_rep
            return True
        return False

def kruskals_mst(V, edges):
    dsu = DSU(V)
    num_circuits = V
    for x, y, _ in edges:
        if dsu.find(x) != dsu.find(y):
            if dsu.union(x, y):
                num_circuits -= 1
        if num_circuits == 1:
            return matrix[x][0]*matrix[y][0]
    return dsu

V = len(matrix)
all_edges = set()
for i in range(V):
    for j in range(i + 1, V):
        p1 = matrix[i]
        p2 = matrix[j]
        weight = (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2
        all_edges.add((i, j, weight))

all_edges = list(all_edges)
all_edges = sorted(all_edges,key=lambda x: x[2])
final_dsu = kruskals_mst(len(matrix), all_edges)
print(final_dsu)


t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))