import webbrowser


class Movie():
    """ this class provides a way to store movie related information"""

    def __init__(
self,  # noqa
movie_title,  # noqa
movie_genre,  # noqa
movie_year,  # noqa
poster_image,  # noqa
trailer_youtube):
        """ self is the obect which is called eg. in this case it points to
toy_story. """
        self.title = movie_title
        self.genre = movie_genre
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        """ by using self. before title or storyline it makes these variable
instance variable but if we remove the self. from any variable that
variable will become local variable we can replace self with any word
for this whole page.
"""

    def show_trailer(self):
        """ this function, show_trailer shows the trailer of the given name of
        the movie which is input when the user clicks on that movie.
"""
        webbrowser.open(self.trailer_youtube_url)
