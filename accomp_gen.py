import music21
import random

c_maj_chord = ["C3", "E3", "G3"]
csharp_min_chord = ["C#3", "E3", "G#3"]
csharp_dim_chord = ["C#3", "E3", "G3"]

d_maj_chord = ["D3", "F#3", "A3"]
d_min_chord = ["D3", "F3", "A3"]

e_maj_chord = ["E3", "G#3", "B3"]
e_min_chord = ["E3", "G3", "B3"]

f_maj_chord = ["F2", "A2", "C3"]
fsharp_min_chord = ["F#2", "A2", "C#3"]
fsharp_dim_chord = ["F#2", "A2", "C3"]

g_maj_chord = ["G2", "B2", "D3"]
gsharp_dim_chord = ["G#2", "B2", "D3"]

a_maj_chord = ["A2", "C#3", "E3"]
a_min_chord = ["A2", "C3", "E3"]

b_min_chord = ["B2", "D3", "F#3"]
b_dim_chord = ["B2", "D3", "F3"]

c_major_chord_progression = [c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord, a_min_chord, b_dim_chord]
g_major_chord_progression = [g_maj_chord, a_min_chord, b_min_chord, c_maj_chord, d_maj_chord, e_min_chord,
                             fsharp_dim_chord]
d_major_chord_progression = [d_maj_chord, e_min_chord, fsharp_min_chord, g_maj_chord, a_maj_chord, b_min_chord,
                             csharp_dim_chord]
a_major_chord_progression = [a_maj_chord, b_min_chord, csharp_min_chord, d_maj_chord, e_maj_chord, fsharp_min_chord,
                             gsharp_dim_chord]

a_minor_chord_progression = [a_min_chord, b_dim_chord, c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord]
e_minor_chord_progression = [e_min_chord, fsharp_dim_chord, g_maj_chord, a_min_chord, b_min_chord, c_maj_chord,
                             d_maj_chord]
b_minor_chord_progression = [b_min_chord, csharp_dim_chord, d_maj_chord, e_min_chord, fsharp_min_chord, g_maj_chord,
                             a_maj_chord]
fsharp_minor_chord_progression = [fsharp_min_chord, gsharp_dim_chord, a_maj_chord, b_min_chord, csharp_min_chord,
                                  d_maj_chord, e_maj_chord]

accomp_stream = music21.stream.Part()
bass_clef = music21.clef.BassClef()
accomp_stream.append(bass_clef)


def generate_accompaniment(chord_progression, key, accomp_rhythm):
    generate_chord_accompaniment(chord_progression, key, accomp_rhythm)
    return accomp_stream


def generate_chord_accompaniment(chord_progression, key, accomp_rhythm):
    if key == 0:
        chord_key = c_major_chord_progression
        print("Key: C Major")
    elif key == 1:
        key_signature = music21.key.KeySignature(1)
        accomp_stream.append(key_signature)
        chord_key = g_major_chord_progression
        print("Key: G Major")
    elif key == 2:
        key_signature = music21.key.KeySignature(2)
        accomp_stream.append(key_signature)
        chord_key = d_major_chord_progression
        print("Key: D Major")
    elif key == 3:
        key_signature = music21.key.KeySignature(3)
        accomp_stream.append(key_signature)
        chord_key = a_major_chord_progression
        print("Key: A Major")
    elif key == 4:
        chord_key = a_minor_chord_progression
        print("Key: A Minor")
    elif key == 5:
        key_signature = music21.key.KeySignature(1)
        accomp_stream.append(key_signature)
        chord_key = e_minor_chord_progression
        print("Key: E Minor")
    elif key == 6:
        key_signature = music21.key.KeySignature(2)
        accomp_stream.append(key_signature)
        chord_key = b_minor_chord_progression
        print("Key: B Minor")
    else:
        key_signature = music21.key.KeySignature(3)
        accomp_stream.append(key_signature)
        chord_key = fsharp_minor_chord_progression
        print("Key: F# Minor")
    # Used for position in note_duration to indicate start and end of each bar
    i = 0
    for chord in chord_progression:
        # Used to count duration in bar
        x = 0
        # While there duration does not equal 4
        while x != 4:
            if (chord-1) == len(chord_key):
                new_chord = music21.chord.Chord(chord_key[chord - 2])
            else:
                # Create new chord based off chord from chord progression
                new_chord = music21.chord.Chord(chord_key[chord - 1])
            # Assign the chord the note duration
            new_chord.duration = accomp_rhythm[i]
            # Add the new chord to the stream
            accomp_stream.append(new_chord)
            # Add note duration used to current duration in bar
            x = x + accomp_rhythm[i].quarterLength
            # Increment position
            i += 1
