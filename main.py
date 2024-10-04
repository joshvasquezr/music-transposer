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