from video_library import VideoLibrary 

class Library:
    def __init__(self):
        self.items = {}

    def add_item(self, key, item):
        self.items[key] = item

    def list_all(self):
        output = ""
        for key, item in self.items.items():
            output += f"{key} {item.info()}\n"
        return output

    def get_item(self, key):
        return self.items.get(key)

    def get_name(self, key):
        item = self.get_item(key)
        return item.name if item else None

    def get_director(self, key):
        item = self.get_item(key)
        return item.director if item else None

    def get_rating(self, key):
        item = self.get_item(key)
        return item.rating if item else -1

    def set_rating(self, key, rating):
        item = self.get_item(key)
        if item:
            item.rating = rating

    def get_play_count(self, key):
        item = self.get_item(key)
        return item.play_count if item else -1

    def increment_play_count(self, key):
        item = self.get_item(key)
        if item:
            item.play_count += 1

library = Library()
library.add_item("01", VideoLibrary("Tom and Jerry", "Fred Quimby", 4))
library.add_item("02", VideoLibrary("Breakfast at Tiffany's", "Blake Edwards", 5))
library.add_item("03", VideoLibrary("Casablanca", "Michael Curtiz", 2))
library.add_item("04", VideoLibrary("The Sound of Music", "Robert Wise", 1))
library.add_item("05", VideoLibrary("Gone with the Wind", "Victor Fleming", 3))