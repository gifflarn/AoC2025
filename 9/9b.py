import time
t0 = time.time()

with open("input.txt", "r") as f:
    inputs = f.readlines()

def is_contained(min_x_rect, max_x_rect, min_y_rect, max_y_rect, vertices, corner1, corner2):
    
    for vertex in vertices:
        if vertex == corner1 or vertex == corner2:
            continue
        x, y = vertex
        if (min_x_rect < x < max_x_rect and min_y_rect < y < max_y_rect):
            return False
    return True

def segments_cross(side, segment):
    (rx1, ry1), (rx2, ry2) = side
    (px1, py1), (px2, py2) = segment
    
    R_X_min, R_X_max = min(rx1, rx2), max(rx1, rx2)
    R_Y_min, R_Y_max = min(ry1, ry2), max(ry1, ry2)
    P_X_min, P_X_max = min(px1, px2), max(px1, px2)
    P_Y_min, P_Y_max = min(py1, py2), max(py1, py2)

    r_is_h = (ry1 == ry2)
    p_is_h = (py1 == py2)
    
    if r_is_h == p_is_h:
        return False

    if r_is_h:
        v_overlap = P_Y_min < ry1 < P_Y_max
        h_overlap = R_X_min < px1 < R_X_max
        
        return h_overlap and v_overlap
        
    else: 
        h_overlap = P_X_min < rx1 < P_X_max
        v_overlap = R_Y_min < py1 < R_Y_max
        
        return h_overlap and v_overlap

vertices = []
max_x = 0
max_y = 0
min_y = float('inf')
min_x = float('inf')
for line in inputs:
    k = line.strip().split(',')
    x, y = int(k[0]), int(k[1])
    vertices.append((x, y))
    max_x = max(x,max_x)
    max_y = max(y,max_y)
    min_y = min(y,min_y)
    min_x = min(x,min_x)

segments = []
for i in range(len(vertices)):
    p1 = vertices[i]
    p2 = vertices[(i + 1) % len(vertices)]
    segments.append((p1, p2))
max_area = 0
best_rectangles = []
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        
        corner1 = vertices[i]
        corner2 = vertices[j]
        
        r_x1, r_y1 = corner1
        r_x2, r_y2 = corner2

        min_x_rect = min(r_x1, r_x2)
        max_x_rect = max(r_x1, r_x2)
        min_y_rect = min(r_y1, r_y2)
        max_y_rect = max(r_y1, r_y2)
        
        width = max_x_rect - min_x_rect
        height = max_y_rect - min_y_rect
        area = (width + 1) * (height + 1)
        
        if is_contained(min_x_rect, max_x_rect, min_y_rect, max_y_rect, vertices, corner1, corner2):
            best_rectangle = {
                'area': area,
                'corners': (corner1, corner2),
                'bounds': (min_x_rect, max_x_rect, min_y_rect, max_y_rect)
            }
            oob = False
            corner3 = (r_x1, r_y2)
            corner4 = (r_x2, r_y1)
            edges = [
                (corner1, corner3),
                (corner3, corner2),
                (corner2, corner4), 
                (corner4, corner1) 
            ]
            for segment in segments:
                for side in edges:
                    if segments_cross(side, segment):
                        oob=True
                        break
                if oob:
                    break
            if oob:
                continue
            best_rectangles.append(best_rectangle)

best_rectangles.sort(key=lambda r: r['area'], reverse=True)
print(best_rectangles[0]["area"])

t1 = time.time()
print("executed in {0:0.1f}ms".format((t1-t0)*1000))

