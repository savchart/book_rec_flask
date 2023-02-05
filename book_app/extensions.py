import argparse
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

from book_app.models import Book

db = SQLAlchemy()


def create_df():
    ratings_path = args.data_folder + 'BX-Book-Ratings.csv'
    books_path = args.data_folder + 'BX-Books.csv'
    ratings = pd.read_csv(ratings_path, encoding='cp1251', sep=';')
    ratings = ratings[ratings['Book-Rating'] != 0]
    books = pd.read_csv(books_path, encoding='cp1251', sep=';', on_bad_lines='skip', low_memory=False)
    books = books[['ISBN', 'Book-Title', 'Book-Author']]
    df_ = pd.merge(ratings, books, on=['ISBN'])
    df_['Book-Title'] = df_['Book-Title'].str.lower()
    df_['Book-Author'] = df_['Book-Author'].str.lower()
    df_.to_csv(f'{args.data_folder}/df.csv', index=False)
    return df_

def create_db(df_):
    db.create_all()
    for i in range(len(df_)):
        db.session.add(Book(
            user_id=df_['User-ID'][i],
            book_title=df_['Book-Title'][i],
            book_author=df_['Book-Author'][i],
            book_rating=df_['Book-Rating'][i]
        ))
    db.session.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_folder', type=str, default='data/')
    args = parser.parse_args()
    df = create_df()
    create_db(df)
