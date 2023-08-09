import imdb

def get_movie_rating(movie_title):
    """
    This function takes in a movie title and returns its rating using the IMDb library.
    """
    ia = imdb.IMDb()
    movie_search = ia.search_movie(movie_title)
    movie_id = movie_search[0].movieID
    movie = ia.get_movie(movie_id)
    rating = movie.data['rating']
    return f"The rating of '{movie_title}' is: {rating}"
    
movie_title = input("Enter the movie title: ")
print(get_movie_rating(movie_title))