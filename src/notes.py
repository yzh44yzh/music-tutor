KEYS = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
WHITE_KEYS = ("C", "D", "E", "F", "G", "A", "B")
BLACK_KEYS_1 = ("C#", "D#")
BLACK_KEYS_2 = ("F#", "G#", "A#")

MATCHING_KEYS = {"C#": "Db",
                 "D#": "Eb",
                 "F#": "Gb",
                 "G#": "Ab",
                 "A#": "Bb"}


# My YAMAHA PSR R300:
# First octave:
# black:    37  39     42  44  46
# white:  36  38  40 41  43  45  47 48
#  1C - 36
#  2C - 48
#  3C - 60
#  4C - 72
#  5C - 84

def parse(Num):
    Octave = ((Num - 36) / 12) + 1
    Pos = (Num - 36) % 12
    return (Octave, KEYS[Pos])
