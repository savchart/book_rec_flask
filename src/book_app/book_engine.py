import pandas as pd
from book_app.utils import query_to_df


class BookProcessor:
    def __init__(self, query):
        self.query = query
        self.df = query_to_df(query)
        self.book_ratings = self.df.groupby("book_title")["book_rating"].mean()

        # Create a new dataframe with the mean rating for each book and the total number of ratings
        self.book_info = pd.DataFrame({"book_title": self.book_ratings.index, "mean_rating": self.book_ratings.values})
        self.book_info["num_ratings"] = self.df["book_title"].value_counts()[self.book_info["book_title"]].values

        # Compute the correlation matrix for the mean ratings of all books take ~10% of the data
        self.corr_matrix = pd.pivot_table(self.df[:5000], values="book_rating", index="user_id", columns="book_title",
                                          fill_value=0).corr(method="pearson", min_periods=10)

    def get_result(self, top_books):
        # Merge the top 10 correlated books with their corresponding mean ratings and number of ratings
        result = pd.merge(pd.DataFrame({"book_title": top_books.index}), self.book_info, on="book_title")
        result = pd.merge(result, self.df[["book_title", "book_author"]], on="book_title")
        result = result.drop_duplicates(subset="book_title")
        result["correlation"] = top_books.values
        return result[["book_title", "book_author", "mean_rating", "correlation"]]

    def find_correlated_books(self, book_title):
        # Select the 10 most correlated books for the given book title
        top_10 = self.corr_matrix[book_title].sort_values(ascending=False).iloc[1:11]
        return self.get_result(top_10)





