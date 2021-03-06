import webbrowser


class Movie():
    """ This class will hold movie information.

    Attributes:
        movie_title: Title of the movie.
        movie_storyline: Storyline of the movie.
        poster_image: Poster image of the movie.
        trailer_youtbe: Youtube link to the trailer of the movie.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
