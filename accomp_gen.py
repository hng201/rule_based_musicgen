import music21, random

c_maj_chord = ["C3", "E3", "G3"]

d_maj_chord = ["D3", "F#3", "A3"]
d_min_chord = ["D3", "F3", "A3"]

e_min_chord = ["E3", "G3", "B3"]

f_maj_chord = ["F2", "A2", "C3"]
fsharp_dim_chord = ["F#2", "A2", "C3"]

g_maj_chord = ["G2", "B2", "D3"]

a_min_chord = ["A2", "C3", "E3"]

b_min_chord = ["B2", "D3", "F#3"]
b_dim_chord = ["B2", "D3", "F3"]

c_major_chord_progression = [c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord, a_min_chord, b_dim_chord]
g_major_chord_progression = [g_maj_chord, a_min_chord, b_min_chord, c_maj_chord, d_maj_chord, e_min_chord, fsharp_dim_chord]

a_minor_chord_progression = [a_min_chord, b_dim_chord, c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord]

accomp_stream = music21.stream.Part()
bass_clef = music21.clef.BassClef()
accomp_stream.append(bass_clef)


def generate_accompaniment(chord_progression, major):
    generate_chord_accompaniment(chord_progression, major)
    return accomp_stream


def generate_chord_accompaniment(chord_progression, major):
    # Random int to decide key
    # For testing limited to number of keys implemented currently
    x = random.randint(0, 1)
    chord_key = []
    # If it is a major chord progression
    if major == True:
        if x == 0:
            chord_key = c_major_chord_progression
            print("Key: C Major")
        else:
            chord_key = g_major_chord_progression
            print("Key: G Major")
    # Select from minor keys
    else:
        chord_key = a_minor_chord_progression
    for chord in chord_progression:
        accomp_stream.append(music21.chord.Chord(chord_key[chord - 1]))
