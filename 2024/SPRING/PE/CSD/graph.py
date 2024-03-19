from collections import defaultdict
from deque import Airport
import heapq

class Flight():
    def __init__(self, ap1, ap2, price):
        """DO NOT MODIFY"""
        self._origin = ap1
        self._destination = ap2
        self._weight = price

    def endpoints(self):
        """Return two endpoints of the edge. DO NOT MODIFY"""
        return (self._origin, self._destination)
    
    def opposite(self, loc):
        """Return other endpoint if loc is one of the endpoints. Otherwise, return None. DO NOT MODIFY"""
        if loc is self._origin:
            return self._destination
        if loc is self._destination:
            return self._origin
        return None
    
    def weight(self):
        """Return weight of the edge. DO NOT MODIFY"""
        return self._weight
    
    def __repr__(self):
        """Representation string of edge. DO NOT MODIFY"""
        endpts = [repr(self._origin), repr(self._destination)]
        repr_str = " <-> ".join(endpts)
        return repr_str

class AirportGraph():
    def __init__(self):
        """
        DO NOT MODIFY
        Graph data example:
        {
            "a": {"b": "a <-> b", "c": "a <-> c", "d": "a <-> d"},
            "b": {"a": "a <-> b"},
            "c": {"a": "a <-> c", "d": "c <-> d"},
            "d": {"a": "a <-> d", "c": "c <-> d"}
        }
        """
        self.data = {}
    
    def display(self):
        """Show current graph data. DO NOT MODIFY"""
        print(self.data)

    def airports(self):
        "Return all the airports in the graph. DO NOT MODIFY"
        return list(self.data.keys())
    
    def flights(self):
        "Return all the flights in the graph. DO NOT MODIFY"
        res = set()
        for airport_flight in self.data.values():
            res.update(airport_flight.values())
        return res
    
    def incident_edges(self, v):
        """Return all flights from and to airport v in the graph. DO NOT MODIFY"""
        return list(self.data[v].values())

    def adjacent_airports(self, v):
        """Return all airports have flights from and to airport v. DO NOT MODIFY"""
        return list(self.data[v].keys())

    def insert_airport(self, code, name=None, city=None, country=None):
        """Insert new airport into the graph
        Args:
            code (str): 3 letters code of the airport
            name (str): name of the airport
            city (str): city which the airport locates
            country (str): country which the airport belongs
        Returns:
            airport (Airport): Airport has been inserted
        """
        # STUDENT IMPLEMENTATION Q2.1
        newairport = Airport(code, name, city, country)
        self.data[newairport] = {}
        return newairport
    
    def insert_flight(self, ap1, ap2, price):
        """Insert new flight into the graph
        Args:
            ap1 (Airport): origin airport
            ap2 (Airport): destination airport
            price (float): Flight price
        """
        # STUDENT IMPLEMENTATION Q2.1
        new_flight = Flight(ap1,ap2,price)
        self.data[ap1][ap2] = new_flight
        self.data[ap2][ap1] = new_flight
    
    
    def bfs(self, start):
        """
        Implementation of breadth-first traversal on a graph
        Args:
            start (Airport): start Airport on the graph
        Returns:
            (dict): dictionary contains levels as keys and 
                    list/set of airports in each level as values
        """
        
        visited = {start:0}
        queue = [(start,0)]
        while queue:
            ap,le = queue.pop(0)    #Airport,length
            for x in self.data[ap]:
                if x not in visited or visited[x] > le + 1 :
                    visited[x] = le+1
                    queue.append((x,le+1))
        
        res = defaultdict(list)
        for ap,le in visited.items():
            res[le].append(ap)
        return dict(res)
    
    
    def shortest_path(self, start, end):
        """
        Find the most economic route between 2 airports on the graph
        Args:
            start (Airport): the start Airport
            end (Airport): the destination Airport
        Returns:
            paths (AirportDeque): list of airports on the most economic route.
            Return None if two airports are not connected.
        """
        # STUDENT IMPLEMENTATION Q2.3
        visited = set()
        myheap = []
        heapq.heappush(myheap,(0,start,[]))
        while myheap:
            dis,cur,path = heapq.heappop(myheap)
            if cur in visited : continue
            visited.add(cur)
            path = path + [cur]
            if cur == end : return dis,path
            for x in self.adjacent_airports(cur):
                total_cost = dis + self.data[cur][x].weight()
                heapq.heappush(myheap,(total_cost,x,path))
        return None
    
    
    def Kruskal(self):
        def findparent(parent,i):
            if parent[i] == i : return i
            return findparent(parent,parent[i])
        def union(parent,rank,x,y):
            rootx = findparent(parent,x)
            rooty = findparent(parent,y)
            if rank[rootx] < rank[rooty] : parent[rootx] = rooty
            elif rank[rooty] < rank[rootx] : parent[rooty] = rootx
            else:
                parent[rooty] = rootx
                rank[x] += 1

        #Add V,E
        verticles = set()
        edges = []
        for x in self.data:
            verticles.add(x)
            for y in self.data[x]:
                edges.append((x,y,self.data[x][y].weight()))
                
        #Sort E, DESC
        edges = sorted(edges,
                       key= lambda x : x[2])
             
        res = []
        i = 0 #index for edges
        e = 0 #index for result
        parent = {}
        rank = {}
        for verticle in verticles :
            parent[verticle] = verticle
            rank[verticle] = 0
        
        for u,v,w in edges:
            rootu = findparent(parent,u)
            rootv = findparent(parent,v)
            
            if rootu != rootv :
                e += 1
                res.append((u,v,w))
                union(parent,rank,u,v)

            if e == len(verticles) :
                break
        
        minimumWeight = 0
        print("Minimum spanning tree")
        for u,v,w in res:
            print(u,v,w)
            minimumWeight += w
        print("Weight of MST:",minimumWeight)
    

def main():
    """Testing for graph"""
    # STUDENT IMPLEMENTATION Q2.1
    # Insert airports and flights from the graph
    mygraph = AirportGraph()
    
    
    DEL=mygraph.insert_airport("DEL", "Indira Gandhi", "New Delhi", "India")
    BKK=mygraph.insert_airport("BKK", "Suvarnabhumi", "Bangkok", "Thailand")
    HAN=mygraph.insert_airport("HAN", "Noi Bai", "Ha Noi", "Vietnam")
    SGN=mygraph.insert_airport("SGN", "Tan Son Nhat", "Ho Chi Minh City", "Vietnam")
    UIH=mygraph.insert_airport("UIH", "Phu Cat", "Quy Nhon", "Vietnam")
    HKG=mygraph.insert_airport("HKG", "Hong Kong", "Hong Kong", "China")
    KUL=mygraph.insert_airport("KUL", "Kuala Lumpur", "Kuala Lumpur", "Malaysia")
    SIN=mygraph.insert_airport("SIN", "Changi", "Singapore", "Singapore")
    ICN=mygraph.insert_airport("ICN", "Incheon", "Seoul", "S.Korea")
    HND=mygraph.insert_airport("HND", "Haneda", "Tokyo", "Japan")

    mygraph.insert_flight(DEL,BKK,4459)
    mygraph.insert_flight(DEL,HAN,4876)
    mygraph.insert_flight(DEL,SGN,2382)
    mygraph.insert_flight(BKK,HAN,4887)
    mygraph.insert_flight(BKK,SGN,6528)
    mygraph.insert_flight(HAN,SGN,1969)
    mygraph.insert_flight(HAN,UIH,3191)
    mygraph.insert_flight(SGN,UIH,1706)
    mygraph.insert_flight(SGN,KUL,5562)
    mygraph.insert_flight(SGN,SIN,6232)
    mygraph.insert_flight(KUL,SIN,1404)
    mygraph.insert_flight(KUL,ICN,2328)
    mygraph.insert_flight(HAN,HKG,1920)
    mygraph.insert_flight(KUL,HKG,2507)
    mygraph.insert_flight(HKG,ICN,2066)
    mygraph.insert_flight(HKG,HND,4039)
    mygraph.insert_flight(HND,ICN,8176)

    

    # STUDENT IMPLEMENTATION Q2.2
    # find cities can be visited from UIH after a direct flight, 1-transit, 2-transits, etc.
    print(mygraph.bfs(UIH))


    # STUDENT IMPLEMENTATION Q2.3
    # find most economic route to travel from UIH to ICN
    print(mygraph.shortest_path(UIH,ICN))
    
    
    mygraph.Kruskal()
if __name__ == "__main__":
    main()
