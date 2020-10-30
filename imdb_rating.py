import imdb
def mov(name_mov):
    ia = imdb.IMDb()
    movie_search = ia.search_movie(name_mov)
    id_movie = movie_search[0].movieID
    series = ia.get_movie(id_movie)
    rating = series.data['rating']
    return f"rating {name_mov} : {rating}"

print(mov(str(input("Name the movie you want to rate:  "))))