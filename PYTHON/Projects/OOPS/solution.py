
class Person:
    def __init__(self, name, contact_info):
        self.name = name
        self.__contact_info = contact_info

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def get_role(self):
        return "Person"

    def __str__(self):
        return f"Name: {self.name} | Contact: {self.get_contact_info()}"


class Book:
    total_books = 0

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.__book_id = book_id
        self.status = True
        Book.total_books += 1

    def get_book_id(self):
        return self.__book_id

    def set_book_id(self, book_id):
        self.__book_id = book_id

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def __str__(self):
        state = "Available" if self.status else "Issued"
        return f"ID: {self.get_book_id()} | Title: {self.title} | Author: {self.author} | Status: {state}"


class Member(Person):
    total_members = 0

    def __init__(self, name, contact_info, member_id):
        super().__init__(name, contact_info)
        self.__member_id = member_id
        self.borrowed_books = []
        Member.total_members += 1

    def get_member_id(self):
        return self.__member_id

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_role(self):
        return "Member - can borrow and return books"

    def borrow_book(self, book):
        if not book.status:
            raise ValueError(f"Book '{book.title}' is already issued.")
        book.status = False
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError(f"'{self.name}' did not borrow '{book.title}'.")
        self.borrowed_books.remove(book)
        book.status = True

    @classmethod
    def get_total_members(cls):
        return cls.total_members

    def __str__(self):
        titles = ", ".join(b.title for b in self.borrowed_books) if self.borrowed_books else "None"
        return (f"MemberID: {self.get_member_id()} | Name: {self.name} | "
                f"Contact: {self.get_contact_info()} | Borrowed: {titles}")


class Librarian(Person):
    def get_role(self):
        return "Librarian - manages books and members"

    def __str__(self):
        return f"Librarian: {self.name} | Contact: {self.get_contact_info()}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    @staticmethod
    def is_valid_book_id(book_id):
        book_id = str(book_id).upper()
        return len(book_id) == 4 and book_id[0] == "B" and book_id[1:].isdigit()

    def add_book(self, title, author, book_id):
        if not title.strip() or not author.strip():
            raise ValueError("Title and author cannot be empty.")
        if not Library.is_valid_book_id(book_id):
            raise ValueError("Invalid book ID format. Use like B001.")
        book_id = book_id.upper()
        if book_id in self.books:
            raise ValueError("A book with this ID already exists.")
        book = Book(title.strip(), author.strip(), book_id)
        self.books[book_id] = book
        return book

    def register_member(self, name, contact_info, member_id):
        if not str(member_id).isdigit():
            raise ValueError("Member ID must be numeric.")
        member_id = str(member_id)
        if member_id in self.members:
            raise ValueError("A member with this ID already exists.")
        member = Member(name.strip(), contact_info.strip(), member_id)
        self.members[member_id] = member
        return member

    def find_book(self, book_id):
        book_id = str(book_id).upper()
        if book_id not in self.books:
            raise LookupError("Book not found.")
        return self.books[book_id]

    def find_member(self, member_id):
        member_id = str(member_id)
        if member_id not in self.members:
            raise LookupError("Member not found.")
        return self.members[member_id]

    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        member.borrow_book(book)
        return book, member

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        member.return_book(book)
        return book, member

    def search_books(self, keyword):
        keyword = keyword.lower().strip()
        if not keyword:
            raise ValueError("Search text cannot be empty.")
        results = [b for b in self.books.values()
                   if keyword in b.title.lower() or keyword in b.author.lower()]
        if not results:
            raise LookupError("No matching books found.")
        return results

    def show_totals(self):
        print(f"\nTotal books: {Book.get_total_books()}")
        print(f"Total members: {Member.get_total_members()}")


def show_menu():
    print("\n" + "=" * 42)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add a new book")
    print("2. Register a new member")
    print("3. Issue a book to a member")
    print("4. Return a book")
    print("5. Search for a book")
    print("6. View total books/members")
    print("7. Check book ID validity")
    print("8. Exit")
    print("=" * 42)


def main():
    library = Library()
    librarian = Librarian("Admin", "admin@library.com")
    print(f"Logged in as: {librarian.get_role()}")

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                book_id = input("Book ID (e.g. B001): ")
                book = library.add_book(title, author, book_id)
                print(f"Added: {book}")

            elif choice == "2":
                name = input("Name: ")
                contact = input("Contact info: ")
                member_id = input("Numeric Member ID: ")
                member = library.register_member(name, contact, member_id)
                print(f"Registered: {member}")
                print(f"Role: {member.get_role()}")

            elif choice == "3":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")
                book, member = library.issue_book(book_id, member_id)
                print(f"Issued '{book.title}' to {member.name}.")

            elif choice == "4":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")
                book, member = library.return_book(book_id, member_id)
                print(f"Returned '{book.title}' from {member.name}.")

            elif choice == "5":
                keyword = input("Search title/author: ")
                for b in library.search_books(keyword):
                    print(b)

            elif choice == "6":
                library.show_totals()

            elif choice == "7":
                book_id = input("Book ID to check: ")
                valid = Library.is_valid_book_id(book_id)
                print("Valid" if valid else "Invalid format (expected B001).")

            elif choice == "8":
                print("Goodbye.")
                break

            else:
                print("Invalid choice, pick 1-8.")

        except ValueError as e:
            print(f"Input error: {e}")
        except LookupError as e:
            print(f"Record error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
