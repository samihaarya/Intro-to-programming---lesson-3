import webbrowser

class Movie():
    def __init__(self, movie_title, movie_genre, movie_storyline, poster_image,trailer_youtube):
        # self is the obect which is called eg. in this case it points to toy_story..
        self.title = movie_title
        self.genre = movie_genre
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#by using self. before title or storyline it makes these variable instance variable but if we remove the self. from any variable that variable will become local variable
#we can replace self with any word for this whole page.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
