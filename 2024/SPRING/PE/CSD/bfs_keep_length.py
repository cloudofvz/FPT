data = {'a': {'b': 4, 'c': 5},
        'b': {'a': 4, 'c': 11, 'e': 7, 'd': 9}, 
        'c': {'a': 5, 'b': 11, 'e': 3}, 
        'e': {'c': 3, 'b': 7, 'd': 13, 'f': 6},
        'd': {'b': 9, 'e': 13, 'f': 2}, 
        'f': {'d': 2, 'e': 6}}



start = 'a'

queue = [(start, 0)]
visited = {start: 0}

while queue:
    (vertex, length) = queue.pop(0)
    for neighbor in data[vertex]:
        if neighbor not in visited or visited[neighbor] > length + 1:
            visited[neighbor] = length + 1
            queue.append((neighbor, length + 1))
            
            
print(visited)

# Output: {'a': 0, 'b': 1, 'c': 1, 'e': 2, 'd': 2, 'f': 3}













    
    
