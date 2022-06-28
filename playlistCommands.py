from masterlistTest import masterlist
import pickle
import os

def createPlaylist():
    PL = []
    PLname = input("What would you like to call the playlist? ")
    if os.path.exists(PLname):
        with open(PLname, "rb") as f:
            PL = pickle.load(f)
createPlaylist()
