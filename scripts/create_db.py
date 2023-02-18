import os
import argparse
import pandas as pd
from sqlalchemy import create_engine


def create_df():
    ratings_path = os.path.join(args.data_folder, 'BX-Book-Ratings.csv')
    books_path = os.path.join(args.data_folder, 'BX-Books.csv')
    ratings = pd.read_csv(ratings_path, encoding='ISO-8859-1', sep=';')
    books = pd.read_csv(books_path, encoding='ISO-8859-1', sep=';', on_bad_lines='skip', low_memory=False)
    ratings = ratings[ratings['Book-Rating'] >= 8]
    books = books[['ISBN', 'Book-Title', 'Book-Author']]
    df_ = pd.merge(ratings, books, on=['ISBN'])
    df_['Book-Title'] = df_['Book-Title'].str.lower()
    df_['Book-Author'] = df_['Book-Author'].str.lower()
    df_ = df_.drop_duplicates()
    df_ = df_.dropna()
    df_ = df_.reset_index(drop=True)
    return df_


def create_db(df_):
    engine = create_engine('sqlite+pysqlite:///app.db')
    df_.columns = ['user_id', 'book_id', 'book_rating', 'book_title', 'book_author']
    df_.to_sql('book', con=engine, index=False, if_exists='replace')


parser = argparse.ArgumentParser()
parser.add_argument('--data_folder', type=str, default='data/')
args = parser.parse_args()
df = create_df()
create_db(df)
