class Location:
    """Class for locations"""
    def __init__(self):
        # STUDENT IMPLEMENTATION Q1.1
        self.prev = None
        self.next = None
        raise NotImplementedError("Method is not implemented")

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
        raise NotImplementedError("Method is not implemented")

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
        raise NotImplementedError("Method is not implemented")
    
    def search_location(self, keyword):
        """
        Search for all locations if their name contains keyword.
        Args:
            keyword (string): keyword to find for a Location.
        Returns:
            res (list[Location]): result list contains Locations, whose names have the keyword.
        """
        # STUDENT IMPLEMENTATION Q1.2
        raise NotImplementedError("Method is not implemented")

    def display(self):
        """
        Show all the locations' names in the linked list.
        """
        # STUDENT IMPLEMENTATION Q1.2
        raise NotImplementedError("Method is not implemented")
