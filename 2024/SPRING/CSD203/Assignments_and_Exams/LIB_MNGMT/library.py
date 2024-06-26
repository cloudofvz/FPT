from avltree import avltree

class LibraryManagement:

    def __init__(self):
        self.books = {} #key = book_id, value = book_data in clude title, author, year
        self.root = None
        self.avl = avltree()
    
    def showBookInfo(self, book_id):
        print(f"{str(book_id).ljust(20)}{self.books[book_id][0].ljust(50)}{self.books[book_id][1].ljust(50)}{str(self.books[book_id][2]).rjust(20)}")

    
    #Insert a book
    def insert(self, book_id, book_data):
        self.root = self.avl.insert(self.root,book_id)
        self.books[book_id] = book_data
    
    #Delete a book  
    def delete(self, book_id):
        self.root = self.avl.delete(self.root, book_id)
        del self.books[book_id]
        
    #Display all books
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.showBookInfo(root.id)
        self.inorder(root.right)
        
    def display(self):
        self.inorder(self.root)
        print()
   
   #Search book by ID     
    def searchbyid(self, book_id):
        if self.avl.search(self.root, book_id):
            self.showBookInfo(book_id)
        else:
            print(f"BOOK WITH ID {book_id} NOT FOUND!\n")
    
    #Search author by keyword
    def searchbyauthor(self, keyword):
        self.found = False
        self.id_traverse_author(self.root, keyword)
        if not self.found:
            print(f"AUTHOR WITH KEYWORD {keyword} NOT FOUND!\n")

    def id_traverse_author(self, root, keyword): # Search the inorder traversal of the tree to find the author
        if not root: return
        self.id_traverse_author(root.left, keyword)
        if keyword.lower() in self.books[root.id][1].lower():
            self.showBookInfo(root.id)
            self.found = True
        self.id_traverse_author(root.right, keyword)


#Write test cases to check the correctness of the operations on the tree.
if __name__ == "__main__":
    mylib = LibraryManagement()
    
    #Inserting books
    mylib.insert(1, ("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    mylib.insert(2, ("To Kill a Mockingbird", "Harper Lee", 1960))
    mylib.insert(3, ("1984", "George Orwell", 1949))
    mylib.insert(4, ("The Catcher in the Rye", "J.D. Salinger", 1951))
    mylib.insert(5, ("The Grapes of Wrath", "John Steinbeck", 1939))
    mylib.insert(6, ("Brave New World", "Aldous Huxley", 1932))
    mylib.insert(7, ("The Lord of the Rings", "J.R.R. Tolkien", 1954))
    mylib.insert(8, ("The Hobbit", "J.R.R. Tolkien", 1937))
    
    #Deleting a book
    mylib.delete(1)
    
    #Displaying all books
    mylib.display()
    
    #Searching a book by ID

    mylib.searchbyid(5) #This book exists
    mylib.searchbyid(1) #This book does not exist
    
    #Searching a book by author
    mylib.searchbyauthor("Tolkien")  #This author exists
    mylib.searchbyauthor("vz")  #This author does not exist