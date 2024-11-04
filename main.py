class Auth():
    userList = []
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.logged_in = False

    #Getter methods
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


    #setter methods
    def set_username(self, newval):
        self.username = newval

    def set_password(self, newval):
        self.password = newval

    @staticmethod
    def register(username, password):
        for user in Auth.userList:
            if user[0] == username:
                print("User already Exists please login instead!!")
                return False
        Auth.userList.append([username, password])
        print("User registered successfully!!")
        return True

    @staticmethod 
    def login(username, password):
        for user in Auth.userList:
            if user[0] == username and user[1] == password:
                print("Logged in successfully!!")
                return True
        print("Invalid credentials")
        return False

class BookRental():
    def __init__(self) -> None:
        self.userList = []
        self.bookList = []
        self.rent_out_books = []
        self.Revenue = 0


    def rent_book(self, book_name):     
        for book in self.bookList:
            if book[0] == book_name:
                self.rent_out_books.append(book)
                self.bookList.remove(book)
                self.Revenue += int(book[3])
                print(self.Revenue)
                print(f"{book[0]} has been rented out!!")
            print("Book not found")


    def add_book(self, book_name, book_author, pages, rent_amount):
        self.bookList.append([book_name, book_author, pages, rent_amount])
        print(f"Book '{book_name}' added successfully!")
                


def main():
    bookList = []
    is_logged_in = False
    book_rental = BookRental()

    while not is_logged_in:
        print("\n~~~~ Authentication Menu ~~~~")
        print("1) Register")
        print("2) Login")
        
        choice = input("Enter your Choice 1 or 2: ")


        if choice == '1':
            username = input("Enter a username for registration: ")
            password = input("Enter a password for registration: ")
            Auth.register(username, password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            is_logged_in = Auth.login(username, password)

        else:
            print("Invalid choice. Please select 1 or 2.")



    while is_logged_in:
        print(f"~~~ * Welcome {(username.upper())} *~~~")
        print("~~~~ Book Menu ~~~~")
        print("1) Add a book")
        print("2) LookUp a book")
        print("3) Display all books")
        print("4) Show all users")
        print("5) Rent a book")
        print("0) Exit")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            print("Adding Book.....")
            book_name = input("Enter book's name: ")
            book_author = input("Enter book's Author: ")
            pages = input("Enter no. of pages in book: ")
            rent_amount = input("Enter the rent rate: ")

            book_rental.add_book(book_name, book_author, pages, rent_amount)

        elif choice == 2:
            print("looking up for a book .....")
            keyword = input("Enter book to lookup: ")

            for book in book_rental.bookList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("~~~~~  All books in My Book store ~~~~")
            print("~~ Available To rent out ~~")
            if len(book_rental.bookList) == 0:
                print("No book to display, Please add a book!!!")

            print("Name\tAuthor\tPages\tRate(ksh)")
            for book in book_rental.bookList:
                print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}")

            print("~~ Rented OUT Books ~~")
            if not book_rental.rent_out_books:
                print("No book to display, Please rent a book!!!")

            print("Name\tAuthor\tPages\tRate(ksh)")
            for book in book_rental.rent_out_books:
                print(f"{book[0]}\t{book[1]}\t{book[2]}\t{book[3]}")

        elif choice == 4:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~*~*~ All Users ~*~*~")
            if len(Auth.userList) > 0:
                indx = 0
                for user in Auth.userList:
                    print(f"{indx}) {user[0]} {user[1]}")
                    indx +=1
            else:
                print("No user available!!, please register!!")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        elif choice == 5:
            print("Renting a book ...")
            book_name = input("Enter a book to rent: ")
            book_rental.rent_book(book_name)
            print("Book rented Succesfully!!!")
            print(f"Total Revenue is: Ksh {book_rental.Revenue}")

if __name__ == "__main__":
    main()