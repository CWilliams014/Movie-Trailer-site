import webbrowser

class Movie():
    """
    This class shows the movie title, trailer,
    story line and poster image
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        """
        This takes in inputs self, movie_title, movie_storyline
        poster_image, trailer_youtube and outputs the link assigned
        to the proper index in entertainment.py
        """
        self.title = movie_title
        """
        Displays movie title, first input in each movie
        in entertainment.py
        """
        self.storyline = movie_storyline
        """
        Gives quick story line, second input in each movie
        in entertainment.py
        """
        self.poster_image_url = poster_image
        """
        Displays movie poster, third input in each movie
        in entertainment.py
        """
        self.trailer_youtube_url = trailer_youtube
        """
        Engages link to youtube url trailer for movie, 4th input
        in each movie in entertainment.py
        """
    

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        """
        calls the function webbrowser.open which is imported
        from import webbrowswer at top of screen
        """
