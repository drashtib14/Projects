class Book:
    def __init__(self,book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_books(self):
        pass

    def display_books(self):
        pass

    def update_book(self):
        pass

    def delete_book(self):
        pass


class Member:
    def borrow_book(self):
        pass
    
    def borrowed_books(self):
        pass

    def return_book(self):
        pass

    def check_due(self):
        pass
    
class Role:
    def run_menu(self):
        while True:
            role = int(input("Enter 1 for Librarian \nEnter 2 for Member\nEnter 3 for Exit\n"))
            if role == 1:
                self.librarian_menu()
                break
            elif role == 2:
                self.member_menu()
                break
            elif role == 3:
                print("Thank you for using the Library!")
                break
            else:
                print("Invalid input. Try again")

    def librarian_menu(self):
        while True:
            print("\n==== Library Menu ====")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Search Book")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                print("Thank you for using the Library!")
                break
            else:
                print("Invalid option. Try again.")

    def member_menu(self):
        while True:
                print("\n==== Library Menu ====")
                print("1. Display Book")
                print("2. Borrow Books")
                print("3. Borrowed Books")
                print("4. return Book")
                print("5. Check due date")
                print("6. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
                    pass
                elif choice == 6:
                    print("Thank you for using the Library!")
                    break
                else:
                    print("Invalid option. Try again.")