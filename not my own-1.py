def displayMainMenu():
  print("")
  print("~~~ Playlist Organiser Menu ~~~")
  print("")
  print("1: View library")
  print("2: Add single track to library")
  print("3. Add multiple tracks to library")
  print("4: Remove track from library")
  print("5: Playlist Manager")
  print("6: Quit")
  print("")


def addSingleTrack():
  print("")

def displayPlaylistMenu():
  print("")
  print("~~~ Playlist Manager ~~~")
  print("")
  print("1: Add new playlist")
  print("2: Amend playlist")
  print("3: Delete playlist")
  print("4: Back to Main Menu")
  print("")
  displayMenuChoice = input("Please choose an option: ")
  

while True:
  displayMainMenu()
  mainMenuChoice = input("Please choose an option: ")
  if mainMenuChoice == "2":
    addSingleTrack()
  elif mainMenuChoice == "5":
    displayPlaylistMenu()
  elif mainMenuChoice == "6":
    break
