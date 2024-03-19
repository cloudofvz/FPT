class Airport:
    """Class for airports"""
    def __init__(self,code,name=None,city=None,country=None):
        # STUDENT IMPLEMENTATION Q1.1
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        
        self.next = None
        self.prev = None

    def __eq__(self, other):
        """for equal comparison. DO NOT MODIFY"""
        if not isinstance(other, Airport):
            return False
        
        if self.code is None:
            return False

        if (self.code, self.name, self.city, self.country) == (other.code, other.name, other.city, other.country):
            return True
        return False
    
    def __ne__(self, other):
        """for not equal comparison. DO NOT MODIFY"""
        return not self == other

    def __repr__(self):
       """Representation string of airport, DO NOT MODIFY"""
       return self.code
        
    def __hash__(self):
        """Hashing objects. DO NOT MODIFY"""
        return hash(id(self))

class AirportDeque:
    """Deque for Airports"""
    def __init__(self):
        self.header = Airport(None, None, None, None)
        self.trailer = Airport(None, None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
    
    def is_empty(self):
        """Check if Deque is Empty"""
        if not self.header.code:
            return True
        return False

    def add_first(self, airport):
        """Add an airport to the front of the deque.
        Args:
            airport (Airport): airport to be added into deque.
        """
        # STUDENT IMPLEMENTATION Q1.2
        newnode = airport
        
        #Case empty
        if self.header.next == self.trailer:
            self.header.next = newnode
            newnode.prev = self.header
            self.trailer.prev = newnode
            newnode.next = self.trailer
        
        #Other cases 
        else:
            first_node = self.header.next
            first_node.prev = newnode
            newnode.prev = self.header
            self.header.next = newnode
            newnode.next = first_node
            
    
    def add_last(self, airport):
        """Add an airport to the back of the deque.
        Args:
            airport (Airport): airport to be added into deque.
        """
        # STUDENT IMPLEMENTATION Q1.2
        newnode = (airport)
        
        #Case empty
        if self.header.next == self.trailer:
            self.header.next = newnode
            newnode.prev = self.header
            self.trailer.prev = newnode
            newnode.next = self.trailer

        #Other case
        else:
            lastnode = self.trailer.prev
            lastnode.next = newnode
            newnode.next = self.trailer
            self.trailer.prev = newnode
            newnode.prev = lastnode
    
    
    def delete_first(self):
        """
        Remove and return the first airport from the deque; an error occurs if the deque is empty.
        Return:
            (Airport): the first airport pushed into the deque. 
            An error occur when the deque is empty.
        """
        # STUDENT IMPLEMENTATION Q1.2
        if self.header.next == self.trailer:
            raise DequeEmpty
        else:
            first_airport = self.header.next
            second_airport = first_airport.next
            second_airport.prev = self.header
            self.header.next = second_airport
            return first_airport
    
    
    
    def delete_last(self):
        """
        Remove and return the last airport from the deque; an error occurs if the deque is empty.
        Return:
            (Airport): the first airport pushed into the deque. 
            An error occur when the deque is empty.
        """
        # STUDENT IMPLEMENTATION Q1.2
        if self.header.next == self.trailer:
            raise DequeEmpty
        else:
            first_to_last = self.trailer.prev
            second_to_last = first_to_last.prev
            second_to_last.next = self.trailer
            self.trailer.prev = second_to_last
            return first_to_last
        
        
    def search_airport(self, keyword):
        """
        Finds all airport in the deque whose names contains the keyword.
        Args:
            keyword (string): keyword to find for an Airport, case-insensitive.
        Returns:
            res (list[Airport]): result list contains Airports, whose names have the keyword.
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
        Show all the airports' codes in the deque.
        """
        # STUDENT IMPLEMENTATION Q1.2
        if self.header.next == self.trailer : return 
        cur = self.header.next
        while cur.code != None:
            print(cur.code)
            cur = cur.next
        
        

class DequeEmpty(Exception):
    """Raise when deque is empty"""
    pass


#Test 
if __name__ == '__main__':
    myairportqueue = AirportDeque()
    myairportqueue.add_last(Airport("DEL", "Indira Gandhi", "New Delhi", "India"))
    myairportqueue.add_last(Airport("BKK", "Suvarnabhumi", "Bangkok", "Thailand"))
    myairportqueue.add_last(Airport("HAN", "Noi Bai", "Ha Noi", "Vietnam"))
    myairportqueue.add_last(Airport("SGN", "Tan Son Nhat", "Ho Chi Minh City", "Vietnam"))
    myairportqueue.add_last(Airport("UIH", "Phu Cat", "Quy Nhon", "Vietnam"))
    myairportqueue.add_last(Airport("HKG", "Hong Kong", "Hong Kong", "China"))
    myairportqueue.add_last(Airport("KUL", "Kuala Lumpur", "Kuala Lumpur", "Malaysia"))
    myairportqueue.add_last(Airport("SIN", "Changi", "Singapore", "Singapore"))
    myairportqueue.add_last(Airport("ICN", "Incheon", "Seoul", "S.Korea"))
    myairportqueue.add_last(Airport("HND", "Haneda", "Tokyo", "Japan"))

    print(myairportqueue.search_airport('K')) #Hong Kong, Kuala
    myairportqueue.display()
