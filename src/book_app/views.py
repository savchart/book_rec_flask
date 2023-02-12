from flask import Blueprint, render_template, request

from book_app.book_engine import BookProcessor
from book_app.models import Book

books = Blueprint("books", __name__, template_folder="C:\\Users\\savchart\\Desktop\\pycharm\\book_rec_flask\\templates")


@books.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_title = request.form["title"]
        user_id = request.form["userid"]
        books_ = Book.query.all()
        book_processor = BookProcessor(books_)
        correlated_books_df = book_processor.find_correlated_books(book_title)
        correlated_books = correlated_books_df.to_dict(orient="records")
        recommended_books_df = book_processor.book_recommendation(user_id)
        return render_template("index.html", correlated_books=correlated_books,
                               recommended_books=recommended_books_df.to_dict(orient="records"))
    return render_template("index.html")
