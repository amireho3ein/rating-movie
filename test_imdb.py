from imdb_rating import *
 
def test_get_movie_rating():
    assert get_movie_rating("Inception") == "The rating of 'Inception' is: 8.8"
    assert get_movie_rating("The Godfather") == "The rating of 'The Godfather' is: 9.2"
    assert get_movie_rating("The Dark Knight") == "The rating of 'The Dark Knight' is: 9.0"
    assert get_movie_rating("Pulp Fiction") == "The rating of 'Pulp Fiction' is: 8.9"
    assert get_movie_rating("Forrest Gump") == "The rating of 'Forrest Gump' is: 8.8"
    print("All tests pass")

if __name__ == "__main__":
    test_get_movie_rating()