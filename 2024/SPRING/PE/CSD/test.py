import heapq

data =  {'a': {'b': 4, 'c': 5}, 
         'b': {'a': 4, 'c': 11, 'e': 7, 'd': 9}, 
         'c': {'a': 5, 'b': 11, 'e': 3}, 
         'e': {'c': 3, 'b': 7, 'd': 13, 'f': 6},
         'd': {'b': 9, 'e': 13, 'f': 2},
         'f': {'d': 2, 'e': 6}}


# Dijkstra's algorithm using priority queue keep track of the shortest path
pq = []
heapq.heappush(pq, (0,'a',[]))
visited = dict()

while pq :
    distance,current,path = heapq.heappop(pq)
    if current in visited.keys() : 
        continue
    visited[current] = (distance,path)
    path = path + [current]
    
    for neighbor in data[current].keys():
        total_cost = distance + data[current][neighbor]
        heapq.heappush(pq, (total_cost, neighbor, path))

print(visited)