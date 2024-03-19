from random import shuffle

#1 - Build a Video class with attributes: video_id, title, description, time
class Video:
    def __init__(self,data):
        self.video_id = data[0]
        self.title = data[1]
        self.description = data[2]
        self.time = data[3]

class Node:
    def __init__(self,data):
            self.prev = None
            if type(data) == list: self.data = Video(data)
            if isinstance(data, Video): self.data = data
            self.next = None

#2 - Build a TikTokPlaylist look like a doubly linked list
class TikTokPlaylist:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        self._ids = []
        
    def addAtHead(self,data):
        newnode = Node(data)
        if self.len == 0 :
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.len += 1
    
    #3 - Add a song to the end of the playlist, duplicate songs are not allowed
    def addAtTail(self,data):
        
        newnode = Node(data)
        if self.len == 0 :
            self.head = newnode
            self.tail = newnode
            self._ids.append(newnode.data.video_id)
        else:
            if newnode.data.video_id not in self._ids:
                self.tail.next = newnode
                newnode.prev = self.tail
                self.tail = newnode
                self._ids.append(newnode.data.video_id)
            else:
                raise IndexError
            
        self.len += 1
    
    def addAtIndex(self,index,data):
        if index < 0 or index > self.len : return
        if index == 0 : return self.addAtHead(data)
        if index == self.len : return self.addAtTail(data)
        i = 0 
        newnode = Node(data)
        cur = self.head
        while i+1 < index :
            cur = cur.next
            i += 1
            
        next_of_cur = cur.next
        cur.next = newnode
        newnode.prev = cur
        newnode.next = next_of_cur
        next_of_cur.prev = newnode
    

    #4 - Remove a and return a song by id
    def remove_and_return_by_id(self,id):
        cur = self.head
        

        
        for i in range(self.len):
            
            #Delete and return
            if cur.data.video_id == id :
                
                if self.len == 1 : #Only have one node
                    self.head = None
                    self._ids.remove(id)
                    self.len -= 1
                    return cur.data.title
                
                if not cur.next : #Tail
                    prev_node = cur.prev
                    prev_node.next = None
                    self._ids.remove(id)
                    self.len -= 1
                    return cur.data.title
                
                if not cur.prev : #Head
                    self.head = cur.next
                    self.head.prev = None
                    self._ids.remove(id)
                    self.len -= 1
                    return cur.data.title   
                
                #Random position                 
                prev_node = cur.prev
                next_node = cur.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self._ids.remove(id)
                self.len -= 1
                return cur.data.title
            
            #Traverse
            cur = cur.next
            
        return "id not present"


    #7 - Remove all songs which title or description has keyword
    def remove_and_by_keyword(self, keyword):
        cur = self.head
        while cur:
            if keyword in cur.data.title or keyword in cur.data.description:
                self.remove_and_return_by_id(cur.data.video_id)
            cur = cur.next
                
    #5 - Display the playlist
    def display(self):
        cur = self.head
        for i in range(self.len):
            print(cur.data.title)
            cur = cur.next
            
    #6 - Search for a song with a keyword
    def search_video(self, keyword):
        cur = self.head
        appear = False
        while cur:
            if keyword in cur.data.title:
                appear = True
            cur = cur.next
        if not appear:
            print(f"There are no songs with the keyword '{keyword}'.")
    
    
    #8 - Shuffle the playlist
    def shuffle_video(self):
        dummy = []
        if not self.head : return
        cur = self.head 
        while cur :
            dummy.append(cur.data)
            cur= cur.next

        #Reset
        self.head = None
        self.tail = None
        self.len = 0
        self._ids = []
        shuffle(dummy)
        for i in range(len(dummy)):
            self.addAtTail(dummy[i])
            
            
#9 - Build a menu to manage the playlist
if __name__ == '__main__':
    mytiktokplaylist = TikTokPlaylist()
    
    #Add 14 songs
    for i in range(1,15):
        data = [f'00{i}',f'Song{i}',f'Des{i}',f'Time{i}']
        mytiktokplaylist.addAtTail(data)
    
    #Shuffle
    print("Shuffle playlist")
    mytiktokplaylist.shuffle_video()
    mytiktokplaylist.display()
    

    print("-------Remove all song which title or descirption has keyword 'g1'----------")
    #Remove by keyword
    mytiktokplaylist.remove_and_by_keyword("g1")
    print("New playlist")
    mytiktokplaylist.display()
    
    print("------Remove and return a song with id 004-----------")
    #Remove by id
    print(mytiktokplaylist.remove_and_return_by_id("004"))
    print("New playlist")
    mytiktokplaylist.display()