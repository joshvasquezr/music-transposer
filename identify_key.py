# What i want to do is feed in a chord progression the program, identify what key we are in...
# Only Major keys for now...


sharp_keys = ["G", "D", "A", "E", "B", "F#", "C#"]
flat_keys = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]

sharp_octave = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
flat_octave = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

scale_key = input("What major scale do you want me to print?")

octave = []
if scale_key in sharp_keys:
    octave = sharp_octave
elif scale_key in flat_keys:
    octave = flat_octave
else:
    octave = flat_octave


one_index = 0
for key in octave:
    if key == scale_key:
        break
    else:
        one_index += 1

scale_octave = []
scale_index = 0
while scale_index < 12:
    if one_index > 11:
        one_index = one_index % 12

    scale_octave.append(octave[one_index])

    if scale_index == 4 or scale_index == 11:
        scale_index += 1
        one_index += 1
    else:
        scale_index += 2
        one_index += 2

print(scale_octave)

