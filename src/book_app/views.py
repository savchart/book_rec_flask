import pandas as pd
import req
from flask import Blueprint, render_template

books = Blueprint("books", __name__, template_folder="templates")


@books.route("/", methods=["GET", "POST"])
def index():
    # get book and author from page
    if request.me


    print('Loading data...')
    data = pd.read_csv(args.df_path)
    print('Getting data...')
    df = get_data(data, args.book, args.author, args.threshold)
    print('Getting recommendations...')
    res = engine(df, args.book)
    return render_template("index.html")
