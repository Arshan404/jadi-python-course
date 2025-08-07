#main.py

from mylibrary.library import Library

def run_libray_system():
    lib = Library()


    while True:
        print("\n--- Library Menu ---")
        print("1. Add a book")
        print("2.Remove book")
        print("3. Search for books")
        print("4. Show all books")
        print("5. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author name: ")
            lib.add_book(title,author)
        elif choice =="2":
            title = title = input("Book title to delete: ")
            lib.remove_book(title)
        elif choice =="3":
            title = input("Book title to search: ")
            lib.search_book(title)
        elif choice =="4":
            lib.show_books()
        elif choice =="5":
            print("Logging out.")
            break
        else:
            print("Invalid option!")

if __name__ =="__main__":
    run_libray_system()            
    

