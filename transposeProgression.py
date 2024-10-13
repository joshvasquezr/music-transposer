from string import whitespace

progression = input("Chord Progression: ")
progressionList = []
for char in progression:
    minor = ""
    if not char.isspace():
        progressionList.append(char)


print(progressionList)

# Do i need to check if a certain chord makes sense...?
# I feel like sometimes there are weird chords in jazz... but if this is for worship and ccm songs, then that's not
# really going to play a factor...
