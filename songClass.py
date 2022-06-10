class Song():
    def __init__(self, name, artist, length, plays):
        self.name = name
        self.artist = artist
        self.length = length
        self.playnum = plays
        self.fav = False

    def toggleFav(self):
        self.fav = not self.fav
