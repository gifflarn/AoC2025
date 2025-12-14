import time
t0 = time.time()
with open("input.txt", "r") as f:
    il = f.readlines()
t_s = []
p = []
n = 0
p_s = dict()
for l in il:
    l = l.strip()
    if not l:
        p_s[n] = pk
        n += 1
        continue
    elif 'x' in l:
        ps = l.split()
        x,y = ps[0].split('x')
        t_s.append((int(x),int(y.strip(":"))))
        p.append([int(p) for p in ps[1:]])
    elif ':' in l:
        pk = 0
    else:
        pk += sum([0 if k == "." else 1 for k in l])
print(sum([1 for (x,y), p_u_t in zip(t_s, p) if not (sum([n_p*p_s[i] for i,n_p in enumerate(p_u_t)]) > x*y or sum([n_p for n_p in p_u_t]) > y//3*x//3)]))
t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))