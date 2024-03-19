import math
import heapq
from linkedlist import Location, LocationLinkedList
from collections import defaultdict

class Edge():
    def __init__(self, loc1, loc2, weight):
        self._origin = loc1
        self._destination = loc2
        self._weight = weight

    def endpoints(self):
        return (self._origin, self._destination)
    
    def opposite(self, loc):
        if loc is self._origin:
            return self._destination
        if loc is self._destination:
            return self._origin
        return None
    
    def weight(self):
        return self._weight
    
    def __repr__(self):
        endpts = [repr(self._origin), repr(self._destination)]
        repr_str = " <-> ".join(endpts)
        return repr_str

class LocationGraph():
    def __init__(self):
        self.data = {}
    
    def display(self):
        print(self.data)

    def locations(self):
        return list(self.data.keys()) 
    
    def edges(self):
        res = set()
        for location_path in self.data.values():
            res.update(location_path.values())
        return res
    
    def incident_edges(self, v):
        return list(self.data[v].values())

    def adjacent_locations(self, v):
        return list(self.data[v].keys())

    def insert_location(self, name, category=None, address=None, description=None):
        newlocation = Location(name,category,address,description)
        self.data[newlocation] = {}
        return newlocation
    
    
    def insert_edge(self, loc1, loc2, weight):
        new_edge = Edge(loc1, loc2, weight)
        self.data[loc1][loc2] = new_edge
        self.data[loc2][loc1] = new_edge
    
    
    def dijkstra(self, start): #Done    
        unvisited = self.locations()
        distances = {loc: math.inf for loc in unvisited}
        distances[start] = 0
        previous = {loc: None for loc in self.data}
        heap = [(0, start)]
        while heap :
            dis,cur = heapq.heappop(heap)
            if cur not in unvisited : continue
            distances[cur] = dis
            unvisited.remove(cur)
            for x in self.adjacent_locations(cur):
                total_cost = dis + self.data[cur][x].weight()
                if total_cost < distances[x]:
                    previous[x] = cur
                    distances[x] = total_cost
                    heapq.heappush(heap,(total_cost,x))

        res = defaultdict(dict)
        for loc in self.locations():
            res[loc] = {}
            res[loc]["Distances"] = distances[loc]
            res[loc]["Previous"] = previous[loc]
        
        return dict(res)
    
    def shortest_path(self, start, end): #Done
        visited = set()
        myheap = []
        heapq.heappush(myheap,(0,start,[]))
        while myheap:
            dis,cur,path = heapq.heappop(myheap)
            if cur in visited : continue
            visited.add(cur)
            path = path + [cur]
            if cur == end : return dis,path
            for x in self.adjacent_locations(cur):
                total_cost = dis + self.data[cur][x].weight()
                heapq.heappush(myheap,(total_cost,x,path))
        return None


    def prim_jarnik(self, start=None): #Done
        unvisited = self.locations()
        if not start:
            start = unvisited[0]
        distances = {loc: math.inf for loc in unvisited}
        distances[start] = 0
        previous = {loc: None for loc in unvisited}
        heap = [(0, start)]

        while heap :
            dis,cur = heapq.heappop(heap)
            if cur not in unvisited or dis > distances[cur] : continue
            unvisited.remove(cur)
            for x in self.adjacent_locations(cur):
                total_cost = dis + self.data[cur][x].weight()
                if x in unvisited and dis + total_cost < distances[x]:
                    distances[x] = total_cost
                    previous[x] = cur
                    heapq.heappush(heap,(total_cost,x))
        
        try :
            res = defaultdict(set)
            for loc in self.locations():
                if loc == start : continue
                res[loc] = (previous[loc],self.data[loc][previous[loc]].weight())
        except:
            return None
        
        res = dict(res)
        if start != None : 
            res[start] = None
        return res
            
    
    def mst_path(self, start, end):
        try:
            mst = self.prim_jarnik(start)
            
            if end not in mst: return None  
            res = [end]
            cur = end
            while mst :
                if cur == start : return res
                res.append(mst[cur][0])
                cur = mst[cur][0]
            
            return None
        except:
            return None

def main():
    G = LocationGraph()
    FSQN = G.insert_location("FPT Software Quy Nhon", "Company")
    QHB=G.insert_location("Quy Hoa Beach", "Beach")
    GRTA=G.insert_location("Ghenh Rang Tourist Area", "Tourist Attraction")
    VCM=G.insert_location("Vung Chua mountain", "Mountain")
    QNS=G.insert_location("Quy Nhon Square", "City Park")
    TD=G.insert_location("Thap Doi", "Heritage Museum")
    BDM=G.insert_location("Binh Dinh Museum", "Museum")
    QNP=G.insert_location("Quy Nhon Port", "Port")
    FU=G.insert_location("FPT University", "University")
    EG=G.insert_location("Eo Gio", "Tourist Attraction")
    KC=G.insert_location("Ky Co", "Beach")

    G.insert_edge(GRTA,QHB,4.4)
    G.insert_edge(GRTA,VCM,4.7)
    G.insert_edge(GRTA,QNS,5.8)
    G.insert_edge(GRTA,FSQN,4.9)
    G.insert_edge(FSQN,QHB,1)
    G.insert_edge(QNS,TD,3.5)
    G.insert_edge(QNS,FU,5.6)
    G.insert_edge(QNS,BDM,1.6)
    G.insert_edge(BDM,QNP,1.4)
    G.insert_edge(QNP,FU,5.2)
    G.insert_edge(FU,EG,17.6)
    G.insert_edge(FU,KC,21.2)
    G.insert_edge(EG,KC,5.9)

    print(G.dijkstra(FSQN))
    
    print(G.shortest_path(FSQN,KC))
    
    print(G.prim_jarnik(FSQN))
    

if __name__ == "__main__":
    main()