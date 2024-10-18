# Music Transposer

**Music Transposer** is a command-line application that allows users to easily transpose chord progressions into any key. It is designed to help musicians quickly shift between keys by adjusting chords according to the specified number of half steps. The program offers customization based on the user's preferred transposition in sharps or flats.

## Features

- Transpose any chord progression to a different key.
- Customize the transposition by specifying the number of half-steps.
- Choose between sharps or flats for the transposed key.

## How It Works

1. The user inputs the current key of the chord progression.
2. The user selects whether they prefer the transposition to be in sharps or flats.
3. The user enters the number of half steps by which they want to transpose the progression.
4. The program outputs the transposed key and chords based on the input.

## Example Usage

```bash
$ python3 music_transposer.py
Enter the current key: C
Would you like the transposed key in sharps or flats? (sharps/flats): sharps
How many half-steps would you like to transpose? 2

The new key is D.
