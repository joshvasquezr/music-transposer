def get_progression():
    progression = input("Chord Progression: ")
    return progression

class TransposeProgression:

    # class-wide variables
    sharpKeys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    flatKeys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    def __init__(self):
        self.currentKeys = []
        self.progressionList = []
        self.userChangeKey = 0
        self.newKey = ""
        self.newProgressionList = []
        self.finalProgressionList = []
        self.newSlashChord = ""
        self.minorChord = False

    def choose_accidental(self):
        choose = True
        while choose:
            sharp_or_flat = input("Would you like to output in terms of sharps or flats? (enter '#' or 'b'): ")

            if sharp_or_flat == '#':
                self.currentKeys = TransposeProgression.sharpKeys
                choose = False
            elif sharp_or_flat == 'b':
                self.currentKeys = TransposeProgression.flatKeys
                choose = False
            else:
                print("Choose '#' or 'b'")

    def change_key(self, chord):
        minor_index = 0
        for char in chord:
            minor_index += 1
            if char == 'm':
                chord = chord[0:minor_index - 1]
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

    def slash_chord(self, slash):
        slash_split = slash.split('/')

        transposed = []
        for chord in slash_split:
            new_slash_chord = self.change_key(chord)
            if self.minorChord:
                new_slash_chord = new_slash_chord + "m"
                self.minorChord = False
            transposed.append(new_slash_chord)

        self.newSlashChord = transposed[0] + '/' + transposed[1]
        return self.newSlashChord

    def transpose_progression(self, progression):
        self.userChangeKey = int(input("Enter the half-steps you would like to change: "))
        self.progressionList = progression.split()

        for chord in self.progressionList:
            if '/' in chord:
                self.newProgressionList.append(chord)
                continue
            new_chord = self.change_key(chord)
            if self.minorChord:
                new_chord = new_chord + "m"
                self.minorChord = False

            self.newProgressionList.append(new_chord)

        for chord in self.newProgressionList:
            if '/' in chord:
                new_slash_chord = self.slash_chord(chord)
                self.finalProgressionList.append(new_slash_chord)
            else:
                self.finalProgressionList.append(chord)



    def main(self):
        self.choose_accidental()
        prog = get_progression()
        self.transpose_progression(prog)
        return self.finalProgressionList

transposeProgression = TransposeProgression()
result = transposeProgression.main()
print(result)