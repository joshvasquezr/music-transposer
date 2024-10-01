sharpKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
flatKeys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb","B"]

test = True

# for i in range(len(flatKeys)):
#     i *= -1
#     print(i, ": ",flatKeys[i])
#
# # breakpoint()

currentKey = input("Enter your current key: ")
# print("Your current key is: ", currentKey)


userChangeKey = input("Enter the half-steps you would like to change: ")
# print("You would like to go: ", changeKey, " steps")

if int(userChangeKey) % 12 == 0:
    print("You would like to go stay in the same key?")
elif int(userChangeKey) > 0:
    print("You would like to go from ", currentKey, " + ", userChangeKey)
elif int(userChangeKey) < 0:
    print("You would like to go from ", currentKey, userChangeKey, " steps")


keyIndex = 0
if int(userChangeKey) < 0:
    changeKey = (int(userChangeKey) * -1) % 12
    changeKey *= -1
else:
    changeKey = int(userChangeKey) % 12

for key in flatKeys:
    if (key == currentKey):
        # print(keyIndex)
        break
    else:
        keyIndex+=1

newKey = keyIndex + int(changeKey)

# case: newKey > len(flatKeys)
if newKey >= len(flatKeys):
    newKey -= 12 # b/c I'm going to move it back to index 0, which will cost 1 index...

print("Ok you're going from", currentKey,"->", flatKeys[newKey])



