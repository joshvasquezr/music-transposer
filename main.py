class Transpose:

    # class-wide variables
    sharpKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    flatKeys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb","B"]

    def __init__(self):
        self.currentKeys = []
        self.currentKey = ""
        self.userChangeKey = 0
        self.newKey = ""

    def choose_accidental(self):
        choose = True
        while choose:
            sharp_or_flat = input("Would you like to output in terms of sharps or flats? (enter '#' or 'b'): ")

            if sharp_or_flat == '#':
                self.currentKeys = Transpose.sharpKeys
                choose = False
            elif sharp_or_flat == 'b':
                self.currentKeys = Transpose.flatKeys
                choose = False
            else:
                print("Choose '#' or 'b'")


    def get_user_key(self):
        self.currentKey = input("Enter your current key: ")

    def change_key(self):
        self.userChangeKey = int(input("Enter the half-steps you would like to change: "))

        if self.userChangeKey % 12 == 0:
            print("You would like to syat in the same key?")
        elif self.userChangeKey > 0:
            print("You would like to go from ", self.currentKey, " + ", self.userChangeKey)
        elif self.userChangeKey < 0:
            print("You would like to go from", self.currentKey, self.userChangeKey)


        key_index = 0
        change_key = self.userChangeKey % 12

        for key in self.currentKeys:
            if key == self.currentKey:
                break
            else:
                key_index += 1

        new_key_index = key_index + change_key

        if new_key_index >= len(self.currentKeys):
            new_key_index -= 12

        self.newKey = self.currentKeys[new_key_index]
        print("Ok you're going from", self.currentKey, "->", self.newKey)

    def main(self):
        self.choose_accidental()
        self.get_user_key()
        self.change_key()

transpose = Transpose()
transpose.main()











































# # ask user if they want sharp or flat key
# goodChoice = True

#
# while goodChoice:
#     sharpOrFlat = input("Would you like this to output in terms of sharps or flats? (enter '#' or 'b'): ")
#
#     if sharpOrFlat == '#':
#         currentKeys = sharpKeys
#         goodChoice = False
#     elif sharpOrFlat == 'b':
#         currentKeys = flatKeys
#         goodChoice = False
#     else:
#         print("Choose '#' or 'b'")
#
# # test = True
#
# currentKey = input("Enter your current key: ")
# # print("Your current key is: ", currentKey)
#
#
# userChangeKey = input("Enter the half-steps you would like to change: ")
# # print("You would like to go: ", changeKey, " steps")
#
# if int(userChangeKey) % 12 == 0:
#     print("You would like to go stay in the same key?")
# elif int(userChangeKey) > 0:
#     print("You would like to go from ", currentKey, " + ", userChangeKey)
# elif int(userChangeKey) < 0:
#     print("You would like to go from ", currentKey, userChangeKey, " steps")
#
#
# keyIndex = 0
# if int(userChangeKey) < 0:
#     changeKey = (int(userChangeKey) * -1) % 12
#     changeKey *= -1
# else:
#     changeKey = int(userChangeKey) % 12
#
# for key in flatKeys:
#     if (key == currentKey):
#         # print(keyIndex)
#         break
#     else:
#         keyIndex+=1
#
# newKey = keyIndex + int(changeKey)
#
# # case: newKey > len(flatKeys)
# if newKey >= len(flatKeys):
#     newKey -= 12 # b/c I'm going to move it back to index 0, which will cost 1 index...
#
# print("Ok you're going from", currentKey,"->", flatKeys[newKey])
#
#
#
# # change keys function
# # key ArrayList Data Members?
# # start program function
# # get user input function
# # change key based on Letter
# # change key based on half-step (or even step) change
#
# """
#
# Object-Oriented
#
# Transpose class
# - Constructor
# - getUserKey
# - changeKey
#
#
# """
#
#
#
#
