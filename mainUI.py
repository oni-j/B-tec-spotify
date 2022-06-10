from masterlistTest import changeformat
from masterlistTest import addsong
from songClass import Song
from masterlistTest import masterlist

def viewMasterlist():
    print(masterlist)
    for song in masterlist:
        print(song.name, song.length)
while True:
    tempCmd = int(input("What would you like to do? \n 1. add to masterlist \n 2. view masterlist")) - 1
    cmdList = ("addsong", "viewMasterlist")
    funcName = cmdList[tempCmd]
    locals()[funcName]()
