
class Location:
    """Class for locations"""
    def __init__(self,name, category = None, address = None, description= None):
        # STUDENT IMPLEMENTATION Q1.1
        self.name = name
        self.category = category
        self.address = address
        self.description = description
        
        self.prev = None
        self.next = None

    def __eq__(self, other):
        """for equal comparison. DO NOT MODIFY"""
        if not isinstance(other, Location):
            return False
        
        if self.name is None:
            return False

        if (self.name, self.category, self.address, self.description) == (other.name, other.category, other.address, other.description):
            return True
        return False
    
    def __ne__(self, other):
        """for not equal comparison. DO NOT MODIFY"""
        return not self == other

    def __repr__(self):
       """Representation string of location, DO NOT MODIFY"""
       return self.name
        
    def __hash__(self):
        """Hashing objects. DO NOT MODIFY"""
        return hash(id(self))

class LocationLinkedList:
    """Linked List for Locations"""
    def __init__(self):
        self.header = Location(None)
        self.trailer = Location(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def add_location(self, location):
        """Add a location to the head of the linked list
        Args:
            location (Location): location to be added
        """
        # STUDENT IMPLEMENTATION Q1.2
        
        #Case empty
        if self.header.next == self.trailer:
            self.header.next = location
            location.prev = self.header
            self.trailer.prev = location
            location.next = self.trailer
        
        #Other cases 
        else:
            first_node = self.header.next
            first_node.prev = location
            location.prev = self.header
            self.header.next = location
            location.next = first_node

    def remove_location(self, name):
        """
        Remove the first location in the linked list have this name, return the location.
        Otherwise, return None.
        Args:
            name (string): name of the Location
        Return:
            (Location): the location has been removed from the linked list. 
            Return None if linked list is empty or no Location object in this linked list has the name.
        """
        # STUDENT IMPLEMENTATION Q1.2
        
        #Case empty
        if self.header.next == self.trailer : return None
        
        cur = self.header.next
        #Traverse the linked list
        while True:
            if cur.name == name:    
                prev_node = cur.prev
                next_node = cur.next
                prev_node.next = next_node
                next_node.prev = prev_node
                return cur 
            
            cur = cur.next
            #Case not found
            if cur == self.trailer:
                return None
                
        
                

    
    def search_location(self, keyword):
        """
        Search for all locations if their name contains keyword.
        Args:
            keyword (string): keyword to find for a Location.
        Returns:
            res (list[Location]): result list contains Locations, whose names have the keyword.
        """
        # STUDENT IMPLEMENTATION Q1.2
        
        if self.header.next == self.trailer : return []
        res = []
        cur = self.header.next
        while cur.code != None:
            if keyword in cur.name:
                res.append(cur)
            cur = cur.next
        
        return res


    def display(self):
        """
        Show all the locations' names in the linked list.
        """
        # STUDENT IMPLEMENTATION Q1.2
        if self.header.next == self.trailer : return 
        cur = self.header.next
        while cur.name != None:
            print(cur.name)
            cur = cur.next
        

if __name__ == '__main__':
    G = LocationLinkedList()
    FSQN = G.add_location(Location("FPT Software Quy Nhon", "Company"))
    QHB=G.add_location(Location("Quy Hoa Beach", "Beach"))
    GRTA=G.add_location(Location("Ghenh Rang Tourist Area", "Tourist Attraction"))
    VCM=G.add_location(Location("Vung Chua mountain", "Mountain"))
    QNS=G.add_location(Location("Quy Nhon Square", "City Park"))
    TD=G.add_location(Location("Thap Doi", "Heritage Museum"))
    BDM=G.add_location(Location("Binh Dinh Museum", "Museum"))
    QNP=G.add_location(Location("Quy Nhon Port", "Port"))
    FU=G.add_location(Location("FPT University", "University"))
    EG=G.add_location(Location("Eo Gio", "Tourist Attraction"))
    KC=G.add_location(Location("Ky Co", "Beach"))
    
    G.remove_location('Thap Doi')
    G.display()