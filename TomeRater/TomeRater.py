class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email for " + self.name + " has now changed to:" + self.email)

    def __repr__(self):
        return "User {name}, email:{email}, books read: {qty}".format(name=self.name, email=self.email,
                                                                      qty=len(self.books))

    def __eq__(self, other_user):
        if (self.name == other_user.name) & (self.email == other_user.email):
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        avg = 0
        total_books = 0
        for value in self.books.values():
            if value:
                avg += value
                total_books += 1
        return avg / total_books


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This books ISBN has been updated.")

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def get_average_rating(self):
        total = 0
        for rate in self.ratings:
            total += rate
        return total / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_book = Fiction(title, author, isbn)
        return new_book

    def create_non_fiction(self, title, subject, level, isbn):
        new_book = Non_Fiction(title, subject, level, isbn)
        return new_book

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            if rating:
                book.add_rating(rating)
        else:
            print("No user with email " + email)

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        email_unique_check = self.users.get(email, None)
        if not email_unique_check:
            self.users[email] = new_user
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("A user with this email already exists.")

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for key in self.users.values():
            print(key)

    def most_read_book(self):
        most_read = 0
        book = None
        for key in self.books.keys():
            if self.books[key] > most_read:
                most_read = self.books[key]
                book = key
        return book

    def highest_rated_book(self):
        highest_rating = 0
        book = None
        for key in self.books.keys():
            if key.get_average_rating() > highest_rating:
                highest_rating = key.get_average_rating()
                book = key
        return book

    def most_positive_user(self):
        highest_avg = 0
        user = None
        for users in self.users.values():
            if users.get_average_rating() > highest_avg:
                highest_avg = users.get_average_rating()
                user = users
        return user
