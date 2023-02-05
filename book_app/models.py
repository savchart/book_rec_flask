from book_app.extensions import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, book_title, book_author, book_rating):
        self.user_id = user_id
        self.title = book_title
        self.author = book_author
        self.rating = book_rating

    def __repr__(self):
        return f"{self.user_id} | {self.title} | {self.author} | {self.rating}"

