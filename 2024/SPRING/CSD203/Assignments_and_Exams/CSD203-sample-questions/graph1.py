import math
import heapq
from deque import Airport, AirportDeque

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
        if code not in self.data:
            airport = Airport(code, name, city, country)
            self.data[airport] = {}
            return airport
        return None
    
    def insert_flight(self, ap1, ap2, price):
        """Insert new flight into the graph
        Args:
            ap1 (Airport): origin airport
            ap2 (Airport): destination airport
            price (float): Flight price
        """
        # STUDENT IMPLEMENTATION Q2.1
        if ap1 in self.data and ap2 in self.data:
            self.data[ap1][ap2] = Flight(ap1, ap2, price)
            self.data[ap2][ap1] = Flight(ap2, ap1, price)
            return True
        return False
        

    def bfs(self, start):
        """
        Implementation of breadth-first traversal on a graph
        Args:
            start (Airport): start Airport on the graph
        Returns:
            (dict): dictionary contains levels as keys and 
                    list/set of airports in each level as values
        """
        # STUDENT IMPLEMENTATION Q2.2
        visited = set()
        queue = []
        level = {}

        level[start] = 0
        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.pop(0)
            for neighbor in self.adjacent_airports(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    level[neighbor] = level[current] + 1
            
        level_dict = {}
        for airport, lvl in level.items():
            if lvl in level_dict:
                level_dict[lvl].append(airport)
            else:
                level_dict[lvl] = [airport]
        
        return level_dict



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
        # STUDENT IMPLEMENTATION Q2.3\
        pq = []
        heapq.heappush(pq, (0, start, []))
        visited = set()

        while pq:
            distance, current, path = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)        
            path = path + [current]

            if current == end:
                return path, distance
            
            for neighbor in self.adjacent_airports(current):
                neighbor_flight = self.data[current][neighbor]
                total_cost = distance + neighbor_flight.weight()
                heapq.heappush(pq, (total_cost, neighbor, path))

        return None

    
    
def main():
    """Testing for graph"""
    # STUDENT IMPLEMENTATION Q2.1
    # Insert airports and flights from the graph
    airPortGraph = AirportGraph()

    DEL = airPortGraph.insert_airport("DEL", "Indira Gandhi", "New Delhi", "India")
    BKK = airPortGraph.insert_airport("BKK", "Suvarnabhumi", "Bangkok", "Thailand")
    HAN = airPortGraph.insert_airport("HAN", "Noi Bai", "Ha Noi", "Vietnam")
    SGN = airPortGraph.insert_airport("SGN", "Tan Son Nhat", "Ho Chi Minh City", "Vietnam")
    UIH = airPortGraph.insert_airport("UIH", "Phu Cat", "Quy Nhon", "Vietnam")
    HKG = airPortGraph.insert_airport("HKG", "Hong Kong", "Hong Kong", "China")
    KUL = airPortGraph.insert_airport("KUL", "Kuala Lumpur", "Kuala Lumpur", "Malaysia")
    SIN = airPortGraph.insert_airport("SIN", "Changi", "Singapore", "Singapore")
    ICN = airPortGraph.insert_airport("ICN", "Incheon", "Seoul", "S.Korea")
    HND = airPortGraph.insert_airport("HND", "Haneda", "Tokyo", "Japan")

    airPortGraph.insert_flight(DEL, BKK, 4459)
    airPortGraph.insert_flight(DEL, HAN, 4876)
    airPortGraph.insert_flight(DEL, SGN, 2382)
    airPortGraph.insert_flight(BKK, HAN, 4887)
    airPortGraph.insert_flight(BKK, SGN, 6528)
    airPortGraph.insert_flight(HAN, SGN, 1969)
    airPortGraph.insert_flight(HAN, UIH, 3191)
    airPortGraph.insert_flight(SGN, UIH, 1706)
    airPortGraph.insert_flight(HAN, HKG, 1920)
    airPortGraph.insert_flight(HKG, HND, 4039)
    airPortGraph.insert_flight(HKG, ICN, 2066)
    airPortGraph.insert_flight(HND, ICN, 8176)
    airPortGraph.insert_flight(HKG, KUL, 2507)
    airPortGraph.insert_flight(ICN, KUL, 2328)
    airPortGraph.insert_flight(SGN, KUL, 5562)
    airPortGraph.insert_flight(SGN, SIN, 6232)
    airPortGraph.insert_flight(SIN, KUL, 1404)

    print(airPortGraph.shortest_path(UIH, ICN))

    # STUDENT IMPLEMENTATION Q2.2
    # find cities can be visited from UIH after a direct flight, 1-transit, 2-transits, etc.
    #

    # STUDENT IMPLEMENTATION Q2.3
    # find most economic route to travel from UIH to ICN
    #
    
if __name__ == "__main__":
    main()