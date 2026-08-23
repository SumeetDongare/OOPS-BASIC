class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def get_category(self):
        if self.rating >= 8:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Movie Collection ---")

        for movie in self.movies:
            print("Movie Name  :", movie.movie_name)
            print("Rating      :", movie.rating)
            print("Ticket Price:", movie.ticket_price)
            print("Category    :", movie.get_category())
            print("------------------------")


# Creating Cinema
cinema = Cinema()

# Adding movies
cinema.add_movie(Movie("Avengers: Endgame", 9.0, 250))
cinema.add_movie(Movie("3 Idiots", 7.5, 180))
cinema.add_movie(Movie("Example Movie", 4.0, 120))

# Displaying movie details
cinema.display_movies()

"""--- Movie Collection ---
Movie Name  : Avengers: Endgame
Rating      : 9.0
Ticket Price: 250
Category    : Hit
------------------------
Movie Name  : 3 Idiots
Rating      : 7.5
Ticket Price: 180
Category    : Average
------------------------
Movie Name  : Example Movie
Rating      : 4.0
Ticket Price: 120
Category    : Flop
------------------------"""