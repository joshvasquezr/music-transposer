sharpKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]

flatKeys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "C"]


currentKey = "E"

keyIndex = 0
for key in flatKeys:
    if (key == "E"):
        print(keyIndex)
        break
    else:
        keyIndex+=1

changeKey = 5

newKey = keyIndex + changeKey

print(flatKeys[newKey])



