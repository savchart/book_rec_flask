from book_app.extensions import db


class Book(db.Model):
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    book_id = db.Column(db.String(42), nullable=False)
    book_rating = db.Column(db.Integer, nullable=False)
    book_title = db.Column(db.String(255), nullable=False)
    book_author = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, book_id, book_rating, book_title, book_author):
        self.user_id = user_id
        self.book_id = book_id
        self.book_rating = book_rating
        self.book_title = book_title
        self.book_author = book_author

    def __repr__(self):
        return f"({self.user_id} | {self.book_id} | {self.book_rating} | {self.book_title} | {self.book_author})"

    def book_to_dict(self):
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "book_rating": self.book_rating,
            "book_title": self.book_title,
            "book_author": self.book_author
        }
