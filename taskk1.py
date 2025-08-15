class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # düz ad

    def __str__(self):
        status = "Mövcuddur" if self.available else "İcarədədir"
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                print("Bu ISBN ilə kitab artıq mövcuddur.")
                return
        self.books.append(book)
        print("Kitab əlavə edildi.")

    def show_books(self):
        if not self.books:
            print("Kitabxanada kitab yoxdur.")
            return
        print("\nKitab siyahısı:")
        for book in self.books:
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"\"{book.title}\" icarəyə verildi.")
                else:
                    print(f"\"{book.title}\" artıq icarədədir.")
                return
        print("Kitab tapılmadı.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"\"{book.title}\" geri qaytarıldı.")
                else:
                    print(f"\"{book.title}\" artıq kitabxanadadır.")
                return
        print("Kitab tapılmadı.")

def main():
    library = Library()
    while True:
        print("\n===== KİTABXANA MENYUSU =====")
        print("1. Kitab əlavə et")
        print("2. Kitabları göstər")
        print("3. Kitab icarəyə götür")
        print("4. Kitabı qaytar")
        print("5. Çıxış")
        choice = input("Seçiminizi daxil edin: ")

        if choice == "1":
            title = input("Kitabın adı: ")
            author = input("Müəllif: ")
            isbn = input("ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            isbn = input("İcarəyə götürmək istədiyiniz kitabın ISBN-i: ")
            library.borrow_book(isbn)

        elif choice == "4":
            isbn = input("Qaytarmaq istədiyiniz kitabın ISBN-i: ")
            library.return_book(isbn)

        elif choice == "5":
            print("Çıxış edilir. Sağ olun!")
            break

        else:
            print("Yanlış seçim, yenidən cəhd edin.")

if __name__ == "__main__":
    main()
