
from songClass import Song
import os
import pickle

masterlist = []
songnumlist = []
IDList = []

if os.path.exists("IDs"):
        with open("IDs", "rb") as f:
            IDList = pickle.load(f)     

if os.path.exists("masterlistFile"):
        with open("masterlistFile", "rb") as f:
                masterlist = pickle.load(f)
        
def update():
    with open("masterlistFile", "wb") as f:
        pickle.dump(masterlist, f)

def changeformat(a, b, c):
    a = str(a)
    b = str(b)

    c = str(c)    
    c = c.split(":")
    c[0] = int(c[0])
    c[1] =  int(c[1])
    c = (c[0] * 60) + c[1]
    SongID = len(IDList)
    IDList.append("a")
    d = SongID
    with open("IDs", "wb") as f:
            pickle.dump(IDList, f)
    return [a, b, c, 0, d]

def addsong():
    song = input("song, artist, length (in the format 0:00)")
    song = song.split(", ")
    temp = changeformat(song[0], song[1], song[2])
    newSong = Song(temp[0], temp[1], temp[2], temp[3], temp[4])
    print(temp)
    masterlist.append(newSong)
    update()

if __name__ == "__main__":

    times = int(input("how many songs to add"))
    for i in range(times):
        addsong()
        
    print(masterlist)
    for song in masterlist:
        print(song.name, song.length, song.ID)

