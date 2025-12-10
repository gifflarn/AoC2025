import time
import math
t0 = time.time()
invalid_ids = set()

with open("input.txt", "r") as f:
    inputs = f.readlines()

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x},{self.y})"

coords = []
for j in inputs:
    k = j.strip().split(',')
    coords.append(Node(int(k[0]),int(k[1])))

vertices = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        c1 = coords[i]
        c2 = coords[j]
        vertices.append((c1,c2))


max_area = 0

for n1,n2 in vertices:
    area = (abs(n1.x-n2.x)+1)*(abs(n1.y-n2.y)+1)
    if area > max_area:
        max_area = area
print(max_area)
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))