import media
import fresh_tomatoes

# Creating a Movie instance for "Inception".
inception = media.Movie("Inception",
                        "One last job could give him his life back but"
                        " only if he can accomplish"
                        " the impossible - inception.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                        "Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# Creating a Movie instance for "Batman Begins".
batman_begins = media.Movie("Batman Begins",
                            "Batman is a superhero that saves people and"
                            " helps stop bad guys.",
                            "https://upload.wikimedia.org/wikipedia/en/a/"
                            "af/Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

# Creating a Movie instance for "The Dark Knight".
dark_knight = media.Movie("The Dark Knight",
                          "Batman is a superhero that saves people and"
                          " helps stop bad guys.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/"
                          "Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# Creating a Movie instance for "The Dark Knight Rises".
dark_knight_raises = media.Movie("The Dark Knight Rises",
                                 "Batman is a superhero that saves people and"
                                 " helps stop bad guys.",
                                 "https://upload.wikimedia.org/wikipedia/en"
                                 "/8/83/Dark_knight_rises_poster.jpg",
                                 "https://www.youtube.com/watch?v=GokKUqLcvD8")  # NOQA

# Creating a Movie instance for "Interstellar".
interstellar = media.Movie("Interstellar",
                           "Trying to save the future of mankind.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/"
                           "Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

# Creating a Movie instance for "Inside Out".
inside_out = media.Movie("Inside Out",
                         "Story of a girls mind.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/"
                         "Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

# Creating a list with all the Movie instances.
movies = [inception, batman_begins, dark_knight, dark_knight_raises,
          interstellar, inside_out]
fresh_tomatoes.open_movies_page(movies)  # Generates webpage with movies.
