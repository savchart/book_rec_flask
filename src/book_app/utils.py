import pandas as pd


def query_to_df(query):
    book_dict = [item.book_to_dict() for item in query]
    df = pd.DataFrame(book_dict, columns=['user_id', 'book_id', 'book_rating', 'book_title', 'book_author'])
    df['user_id'] = df['user_id'].astype('int32')
    df['book_rating'] = df['book_rating'].astype('int8')
    return df
