class Movie():
    """Class that represents a Movie"""
    def __init__(self, movie_title, storyline, poster_image,
                 trailer_youtube, duration):
        """Inits all data of a movie
        Args:
            movie_title(str): Movie title
            storyline(str): Movie storyline
            poster_image(str): Movie poster image
            trailer_youtube(str): Movie youtube url
            duration(str): Duration of the movie
        """
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = duration
