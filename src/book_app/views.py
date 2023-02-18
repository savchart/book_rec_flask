from flask import Blueprint, render_template, request

from book_app.book_engine import BookProcessor
from book_app.models import Book

books = Blueprint("books", __name__, template_folder="../../templates")


@books.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_title = request.form["title"]
        books_ = Book.query.all()
        book_processor = BookProcessor(books_)
        correlated_books_df = book_processor.find_correlated_books(book_title)
        return render_template("index.html",
                               correlated_books=correlated_books_df.to_dict(orient="records"))
    return render_template("index.html")
