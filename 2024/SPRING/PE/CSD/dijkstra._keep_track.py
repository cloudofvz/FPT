import heapq
from collections import defaultdict
# data =  {'a': {'b': 4, 'c': 5}, 
#          'b': {'a': 4, 'c': 11, 'e': 7, 'd': 9}, 
#          'c': {'a': 5, 'b': 11, 'e': 3}, 
#          'e': {'c': 3, 'b': 7, 'd': 13, 'f': 6},
#          'd': {'b': 9, 'e': 13, 'f': 2},
#          'f': {'d': 2, 'e': 6}}

data = defaultdict(dict)
handle = open("./path.txt",'r')
for line in handle:
    line = line.strip()
    start,end,cost = line.split()
    cost = int(cost)
    data[start][end] = cost
    data[end][start] = cost



myheap = []
heapq.heappush(myheap,(0,'a',[]))
visited = set()

res = {}
while myheap :
    dis,cur,path = heapq.heappop(myheap)
    if cur in visited : 
        continue
    visited.add(cur)
    path = path + [cur]
    res[cur] = (dis,path)
    for nearby,cost in data[cur].items():
        totalcost = dis+cost
        heapq.heappush(myheap,(totalcost,nearby,path))

for k,v in res.items():
    print(k,':',v[0],'->'.join(v[1]))