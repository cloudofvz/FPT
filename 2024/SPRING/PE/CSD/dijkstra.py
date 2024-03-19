from collections import defaultdict
handle = open('./path.txt')

data = defaultdict(dict)

for line in handle :
    line = line.strip()
    x,y,cost = line.split()
    cost = int(cost)
    data[x][y] = cost
    data[y][x] = cost


res = {}
for k in data.keys():
    res[k] = float('inf')


visited = set()
queue = []
queue.append('a')
res['a'] = 0
while queue != []:
    cur = queue.pop(0)
    visited.add(cur)
    for nearby,cost in data[cur].items():
        res[nearby] = min(res[nearby],res[cur]+cost)
        if nearby not in visited:
            queue.append(nearby)

print(res)

        