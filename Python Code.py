class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("\t" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"Your book have been issued {bookName}.\n Please return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait unti the book is returned")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returning {bookname} book")


class Student:
    def requestBook(self):
        self.book = input("Enter the book you want  to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book you want  to return: ")
        return self.book



if __name__ == "__main__":
    centraLibrary = Library(["Python", "SQL", "Excel", "Front-end"])
    # centraLibrary.displayAvailableBooks()
    student = Student()

    while(True):
        welcomemsg = '''====Welcome to Central Library====
        Please choose an option
        1. List of all books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library'''
        print(welcomemsg)

        a = int(input("Enter a choice"))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook(student.requestBook())
        elif a==3:
            centraLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for using this library ")
            exit()
        else:
            print("Invalid choice")




