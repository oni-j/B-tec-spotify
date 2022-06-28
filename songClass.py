class Song():
    def __init__(self, name, artist, length, plays, ID):
        self.name = name
        self.artist = artist
        self.length = length
        self.playnum = plays
        self.fav = False
        self.ID = ID

    def toggleFav(self):
        self.fav = not self.fav
