import sqlite3
import json
class Library:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                is_borrowed INTEGER
            )
        """)
        self.connection.commit()
    def add_book(self, title, author, is_borrowed=0):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.cursor.execute("INSERT INTO books (title, author, is_borrowed) VALUES (?, ?, ?)", (self.title, self.author, self.is_borrowed))
        self.connection.commit()
    
    def list_book(self):
        result = self.cursor.execute("SELECT * FROM books")
        rows = result.fetchall()
        books = []
        for row in rows:
            book = {"id" : row[0], "title" : row[1], "author" : row[2], "is_borrowed" : row[3]}
            books.append(book)
        return books
    
    
    def borrow_book(self, req_id):
        self.id = req_id
        self.cursor.execute("UPDATE books SET is_borrowed = 1 WHERE id = ?", (self.id,))
        self.connection.commit()
        
        
    def return_book(self, req_id):
        self.cursor.execute("UPDATE books SET is_borrowed = 0 WHERE id = ?", (req_id,))
        self.connection.commit()
    
    
lib = Library("library.db")

def inter_face():
            print("1. Add a book")
            print("2. List all books")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. Exit")
def main():
        while True:
            inter_face()
            check = True    
            while check: 
                try:
                    choice = int(input())
                    check = False
                except:
                    print("please write a valid number !!! ")
                    check = True
            if choice == 1:
                writer = input("please write the title name: ")
                author = input("please write the author name: ")
                lib.add_book(writer, author)
            elif choice == 2:
                print(lib.list_book())
            elif choice == 3:
                check = True
                while check:
                    try:
                        book_id = int(input("please write your book id: "))
                        lib.borrow_book(book_id)
                        print("the book is succesfully added on your profile")
                        check = False
                    except:
                        print("please enter the valid number of your book id !!!")
                        check = True
            elif choice == 4:
                check = True
                while check:
                    try:
                        book_id = int(input("please write your book id: "))
                        lib.return_book(book_id)
                        print("you succesfully returned the book to the library")
                        check = False
                    except:
                        print("please enter the valid number of your book id !!!")
                        check = True
            elif choice == 5:
                break
            
        with open("library_db.json", "w") as file:
            json.dump(lib.list_book(), file)
if __name__ == "__main__":
    main()