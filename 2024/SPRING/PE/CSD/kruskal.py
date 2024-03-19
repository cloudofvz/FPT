from collections import defaultdict


class Graph:
    def __init__(self):
        self.V = set()
        self.graph = []
    
    def addedge(self,u,v,w):
        self.graph.append([u,v,w])
        self.V.add(u)
        self.V.add(v)
        
    def findparent(self,parent,i):
        if parent[i] == parent : return i
        return self.findparent(parent,parent[i])

    def union(self,parent,rank,x,y):
        rootx = self.findparent(parent,x)
        rooty = self.findparent(parent,y)
        
        if rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        elif rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        else:
            parent[rooty] = rootx
            rank[x] += 1
    
    def Kruskal(self):
        res = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,
                            key=lambda x: x[2])
        parent = []
        rank = []
        for node in self.V :
            parent.append(node)
            rank.append(0)
            
        while e < len(self.V) - 1 :
            u,v,w = Graph()