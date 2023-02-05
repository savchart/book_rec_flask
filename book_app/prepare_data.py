def get_author_readers(df_, b_title, b_author):
    a_readers = df_['User-ID'][(df_['Book-Title'] == b_title) & (df_['Book-Author'].str.contains(b_author))]
    a_readers = a_readers.unique().tolist()
    books_a_readers_ = df_[(df_['User-ID'].isin(a_readers))]
    return books_a_readers_


def get_books_to_compare(books_a_readers_, threshold_):
    number_of_rating_per_book = books_a_readers_.groupby(['Book-Title']).agg('count').reset_index()
    books_to_compare_ = number_of_rating_per_book['Book-Title'][number_of_rating_per_book['User-ID'] >= threshold_]
    books_to_compare_ = books_to_compare_.tolist()
    return books_to_compare_


def get_ratings_data(books_a_readers_, books_to_compare_):
    ratings_data_raw = books_a_readers_[['User-ID', 'Book-Rating', 'Book-Title']][
        books_a_readers_['Book-Title'].isin(books_to_compare_)]
    return ratings_data_raw


def get_ratings_data_nodup(ratings_data_raw):
    ratings_data_raw_nodup_ = ratings_data_raw.groupby(['User-ID', 'Book-Title'])['Book-Rating'].mean()
    ratings_data_raw_nodup_ = ratings_data_raw_nodup_.to_frame().reset_index()
    return ratings_data_raw_nodup_


def get_data(df, b_title, b_author, threshold_):
    books_a_readers = get_author_readers(df, b_title, b_author)
    books_to_compare = get_books_to_compare(books_a_readers, threshold_)
    ratings_raw = get_ratings_data(books_a_readers, books_to_compare)
    ratings_data_raw_nodup = get_ratings_data_nodup(ratings_raw)
    return ratings_data_raw_nodup
