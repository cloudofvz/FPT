from mutagen.mp3 import MP3
import os
def get_mp3_metadata(file):
    try:
        audio = MP3(file)
        title = str(audio["TIT2"])
        artist = str(audio["TPE1"])
        album = str(audio["TALB"])
        duration = str(round(audio.info.length)) 
        return title, artist, album, duration
    except Exception as e:
        return None
    


class Song:
    def __init__(self,file):
        self.path = file
        audio = MP3(file)
        self.title = str(audio["TIT2"])
        self.artist = str(audio["TPE1"])
        self.album = str(audio["TALB"])
        self.duration = str(round(audio.info.length)) 


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class List_song:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.lenght = 0       

    def addToHead(self, x): # thêm một nút có giá trị x vào đầu .
        new_node = Node(x)  
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next =self.head
            self.head = new_node
            self.head.next.prev = new_node
        self.lenght += 1

    def addToTail(self, x): # thêm một nút có giá trị x vào cuối .
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            print(self.head.data)
            new_node.prev = self.tail
            print(self.head.data)
            self.tail = new_node
            print(self.head.data)
        self.lenght += 1

    def changee(self,node):
        pass

    def traverse(self): # duyệt từ đầu -> cuối và hiển thị thông tin của tất cả các nút trong danh sách.
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def traverseld(self): # duyệt từ đầu -> cuối và hiển thị thông tin của tất cả các nút trong danh sách.
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")
def get_files_in_directory(directory):
    files = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        _, file_extension = os.path.splitext(full_path)
        if os.path.isfile(full_path) and file_extension== '.mp3':
            files.append(get_mp3_metadata(full_path))
    return files

    

# # Đường dẫn đến thư mục bạn muốn lấy tệp
# directory_path = "list_song"
# files = get_files_in_directory(directory_path)
# print(files)


aa =List_song()

aa.addToTail(0)
aa.addToTail(4)
# aa.addToTail(9)
# aa.addToTail(5)
# aa.addToTail(3)
# aa.addToTail(2)
# aa.traverse()
# aa.traverseld()
# print(aa.head.data,'      ',aa.tail.data)