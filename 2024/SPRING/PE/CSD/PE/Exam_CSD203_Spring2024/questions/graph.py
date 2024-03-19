import math
import heapq
from linkedlist import Location, LocationLinkedList

class Edge():
    def __init__(self, loc1, loc2, weight):
        """DO NOT MODIFY"""
        self._origin = loc1
        self._destination = loc2
        self._weight = weight

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

class LocationGraph():
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

    def locations(self):
        "Return all the locations in the graph. DO NOT MODIFY"
        return list(self.data.keys())
    
    def edges(self):
        "Return all the edges in the graph. DO NOT MODIFY"
        res = set()
        for location_path in self.data.values():
            res.update(location_path.values())
        return res
    
    def incident_edges(self, v):
        """Return all edges incident to location v in the graph. DO NOT MODIFY"""
        return list(self.data[v].values())

    def adjacent_locations(self, v):
        """Return all locations adjacent to location v in the graph. DO NOT MODIFY"""
        return list(self.data[v].keys())

    def insert_location(self, name, category=None, address=None, description=None):
        """Insert new location into the graph
        Args:
            name (str): Name of the location
            category (str): Category of the location
            address (str): Location's address
            description (str): Location's description
        Returns:
            loc (Location): Location has been inserted
        """
        # STUDENT IMPLEMENTATION Q2.1
        raise NotImplementedError("Method is not implemented")
    
    def insert_edge(self, loc1, loc2, weight):
        """Insert new edge into the graph
        Args:
            loc1 (Location): origin location
            loc2 (Location): destination location 
            weight (float): Edge weight
        """
        # STUDENT IMPLEMENTATION Q2.1
        raise NotImplementedError("Method is not implemented")
    
    def dijkstra(self, start):
        """
        Implementation of dijksta algorithm
        Args:
            start (Location): start Location on the graph
        Returns:
            (dict): distances and previous Location of each location   
            {"distances": ..., "previous": ...}
        """
        # Initialized a list of unvisited locations
        unvisited = self.locations()
        # Initialize a dictionary of location and their shortest distances to start.
        # At first every location has an infinity distance, except for distance[start] is 0. 
        distances = {loc: math.inf for loc in unvisited}
        distances[start] = 0
        # Initialize a dictionary contains previous location of each location. This will help find the path.
        previous = {loc: None for loc in self.data}
        # heap work as priority queue
        heap = [(0, start)]

        # STUDENT IMPLEMENTATION Q2.2
        # Dijkstra's Loop
        # When heap is not empty:
        #   Extract the location which has min distance from heap using heapq.heappop(heap)
        #   In case of min distance larger than saved distance, continue 
        #   Remove this location from unvisited
        #   Explore unvisited adjacent locations of this location.
        #       If the distance of current location + weight of edge between 2 locations smaller than the distances' value, implement
        #            Update the distance of adjacent location
        #            Update the previous of adjacent location is the current location
        #            Insert to the heap with heapq.heappush(heap, (new distance, adjacent location))
        raise NotImplementedError("Method is not implemented")
    
    def shortest_path(self, start, end):
        """
        Find the shortest path between 2 locations on the graph
        Args:
            start (Location): the start Location
            end (Location): the destination Location
        Returns:
            paths (LocationLinkedList): list of locations on the shortest path.
            Return None if two locations are not connected.
        """
        # STUDENT IMPLEMENTATION Q2.2
        raise NotImplementedError("Method is not implemented")

    def prim_jarnik(self, start=None):
        """Implementation of prim_jarnik algorithm
        Args:
            start (Location): start Location on the graph. Default to None
        Returns:
            mst(dict): minimum spanning tree as a dictionary, contains previous Location and edge between 
            {location: (previous, edge(previous, location))}
        """
        # Initialized a list of unvisited locations
        unvisited = self.locations()
        # If start is not defined, set start as the first locations in graph data (which is random)
        if not start:
            start = unvisited[0]
        # Initialize a dictionary of location and their shortest distances to visited locations.
        # At first every location has a infinity distance, except for distances[start] is 0.
        distances = {loc: math.inf for loc in unvisited}
        distances[start] = 0
        # Initialize a dictionary contains previous location of each location. This will help find the path.
        previous = {loc: None for loc in unvisited}
        # heap work as priority queue
        heap = [(0, start)]

        # STUDENT IMPLEMENTATION Q2.3
        # Prim's algorithm loop
        # When heap is not empty:
        #   Extract the location which has min distance from heap using heapq.heappop(heap)
        #   If the location is visited, continue
        #   Remove this location from unvisited
        #   Explore the adjacent locations of current location
        #       If location is not visited and the edge between has a lower weight than the saved distance
        #           Update the distances of adjacent locations.
        #           Update the previous of adjacent location is the current location
        #           Update the heap with heapq.heappush(head, (new distance, adjacent location))
        # Construct the minimum spanning tree mst as a dictionary:
        #       keys are location
        #       values are (previous location, edge between location and previous location)
        # previous location shouldn't be None, except for the start
        raise NotImplementedError("Method is not implemented")

    
    def mst_path(self, start, end):
        """
        Find the path between 2 locations on the graph using its minimum spanning tree
        Args:
            start (Location): the start Location
            end (Location): the destination Location
        Returns:
            paths (LocationLinkedList): list of locations on the mst path.
            Return None if two locations are not connected.
        """
        # STUDENT IMPLEMENTATION Q2.3
        raise NotImplementedError("Method is not implemented")
    
def main():
    """Testing for graph"""
    # STUDENT IMPLEMENTATION Q2.1
    # Insert locations and edges from the graph
    # ("FPT Software Quy Nhon", "Company")
    # ("Quy Hoa Beach", "Beach")
    # ("Ghenh Rang Tourist Area", "Tourist Attraction")
    # ("Vung Chua mountain", "Mountain")
    # ("Quy Nhon Square", "City Park")
    # ("Thap Doi", "Heritage Museum")
    # ("Binh Dinh Museum", "Museum")
    # ("Quy Nhon Port", "Port")
    # ("FPT University", "University")
    # ("Eo Gio", "Tourist Attraction")
    # ("Ky Co", "Beach")
    raise NotImplementedError("Method is not implemented")

    # (Optional) For testing purpose
    # Find the shortest past between FPT Software and FPT University 

    # Find the mst past between FPT Software and FPT University
    
if __name__ == "__main__":
    main()