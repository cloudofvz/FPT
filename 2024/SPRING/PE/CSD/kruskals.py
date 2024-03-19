from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.vertices = set()

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
        self.vertices.add(u)
        self.vertices.add(v)

    def find(self, parent, i):
        if parent[i] == i: return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []

        edges = []

        for x in self.graph:
            for y in self.graph[x]:
                edges.append((x,y,self.graph[x][y]))
        
        edges.sort(key=lambda x: x[2])

        parent = {}
        rank = {}
        for vertice in self.vertices:
            parent[vertice] = vertice
            rank[vertice] = 0

        e = 0
        for u, v, w in edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

            if e == len(self.vertices) - 1:
                break

        print("Cây bao phủ nhỏ nhất:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


# Ví dụ minh họa
g = Graph()
g.add_edge('Nhon Binh', 'Nhon Phu', 2)
g.add_edge('Nhon Binh', 'Dong Da', 5)
g.add_edge('Nhon Binh', 'Tran Quang Dieu', 6)
g.add_edge('Nhon Phu', 'Tran Quang Dieu', 7)
g.add_edge('Dong Da', 'Hai Cang', 4)
g.add_edge('Dong Da', 'Quang Trung', 4)
g.add_edge('Dong Da', 'Thi Nai', 2)
g.add_edge('Hai Cang', 'Thi Nai', 3)
g.add_edge('Nhon Phu', 'Quang Trung', 6)
g.add_edge('Tran Quang Dieu', 'Bui Thi Xuan', 4)
g.add_edge('Bui Thi Xuan', 'Quang Trung', 8)
g.add_edge('Bui Thi Xuan', 'Ghenh Rang', 9)
g.add_edge('Quang Trung', 'Trung Tam', 3)
g.add_edge('Trung Tam', 'Ghenh Rang', 4)
g.add_edge('Thi Nai', 'Trung Tam', 1)
g.add_edge('Quang Trung', 'Ghenh Rang', 7)
g.kruskal()
