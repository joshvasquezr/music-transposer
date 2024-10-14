def get_progression():
    progression = input("Chord Progression: ")
    return progression

class TransposeProgression:

    def __init__(self):
        self.currentKeys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
        self.progressionList = []
        self.userChangeKey = 0
        self.newKey = ""
        self.newProgressionList = []
        self.minorChord = False


    def change_key(self, chord):
        if len(chord) > 1:
            chord = chord[0]
            self.minorChord = True

        key_index = 0
        change_key = self.userChangeKey % 12 # 25 % 12 = 1

        for key in self.currentKeys:
            if key == chord:
                break
            else:
                key_index += 1

        new_key_index = key_index + change_key

        if new_key_index >= len(self.currentKeys):
            new_key_index -= 12

        self.newKey = self.currentKeys[new_key_index]
        return self.newKey

    def transpose_progression(self, progression):
        self.userChangeKey = int(input("Enter the half-steps you would like to change: "))
        self.progressionList = progression.split()

        for chord in self.progressionList:
            new_chord = self.change_key(chord)
            if self.minorChord:
                new_chord = new_chord + chord[1:]
                self.minorChord = False

            self.newProgressionList.append(new_chord)

    def main(self):
        prog = get_progression()
        self.transpose_progression(prog)
        return self.newProgressionList

transposeProgression = TransposeProgression()
result = transposeProgression.main()
print(result)