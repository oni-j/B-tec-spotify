from masterlistTest import masterlist
import pickle
import os

playlistList = {}

if os.path.exists("playlistList"):
    with open("playlistList", "rb") as f:
        playlistList = pickle.load(f)

def createPlaylist():
    PLname = input("What would you like to call the playlist? ")
    playlistList[PLname] = []
    if os.path.exists("playlistList"):
        with open("playlistList", "wb") as f:
            pickle.dump(playlistList, f)
            

def playlistUpdate():
    PLTemp = []
    IDList = []
    updatedPL = input("What playlist to update? ")
    if updatedPL in playlistList:
        iterationNum = int(input("how many songs to add? "))
        for song in masterlist:
            print(song.name, song.artist, "id:", song.ID)
            IDList.append(song.ID)
        print("input the ids of the songs you want to add")
        for i in (0, iterationNum):
            IDAdd = input("")
            if IDAdd in IDList:
                playlistList[updatedPL].append(IDAdd)
    else:
        print("That playlist does not exist")

if __name__ == "__main__":
    createPlaylist()
    print(playlistList)
    playlistUpdate()
