from itertools import permutations
citys = [
    (0,0),(0,1),(0,2),(0,3)
    (1,0),            (1,3),
    (2,0),            (2,3),
    (3,0),(3,1),(3,2),(3,3) 
    ]

path = [i for i in range(len(citys))]
print(path)

def distance(p1, p2):
    print('p1=', p1)
    x1, y1 = p1
    x2, y2 = p2

    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p,citys):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
    return dist

best_path = None
min_distance = float('inf')
n=0
for path in permutations(range(len(citys))):
    current_distance = pathLength(path, citys)
    n=n+1
    print(n)
    if current_distance < min_distance:
        min_distance = current_distance
        best_path = path

print("Best Path:", best_path)
print("Min Distance:", min_distance)

