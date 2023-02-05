def get_corr_matrix(ratings_data_raw_nodup_):
    book_ratings = ratings_data_raw_nodup_.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating')
    corr_matrix_ = book_ratings.corr(method='pearson', min_periods=10)
    return corr_matrix_


def get_corr_for_book(corr_matrix_, book_):
    book_list = corr_matrix_[book_].sort_values(ascending=False).index.tolist()
    book_corr = corr_matrix_[book_].sort_values(ascending=False).tolist()
    result_list_ = list(zip(book_list, book_corr))
    return result_list_


def engine(ratings_data_raw_nodup, book_):
    corr_matrix = get_corr_matrix(ratings_data_raw_nodup)
    result_list = get_corr_for_book(corr_matrix, book_)
    return result_list
