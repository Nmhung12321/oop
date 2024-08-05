# Define a class to represent a library item (e.g. a video)
class LibraryItem:
    # Initialize a new library item with a name, director, and optional rating
    def __init__(self, name, director, rating=0):
        # Store the name of the library item
        self.name = name
        # Store the director of the library item
        self.director = director
        # Store the rating of the library item (default is 0)
        self.rating = rating
        # Initialize the play count to 0
        self.play_count = 0

    # Return a string with information about the library item
    def info(self):
        # Use an f-string to format the string with the name, director, and rating
        return f"{self.name} - {self.director} {self.stars()}"

    # Return a string with the rating represented as stars
    def stars(self):
        # Initialize an empty string to store the stars
        stars = ""
        # Loop through the rating and add a star for each point
        for i in range(self.rating):
            # Add a star to the string
            stars += "*"
        # Return the string of stars
        return stars