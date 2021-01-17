import music21

c_chord = ["C3", "E3", "G3"]
d_min_chord = ["D3", "F3", "A3"]
e_min_chord = ["E3", "G3", "B3"]
f_maj_chord = ["F2", "A2", "C3"]
g_maj_chord = ["G2", "B2", "D3"]
a_min_chord = ["A2", "C3", "E3"]
b_dim_chord = ["B2", "D3", "F3"]
c_major_chord_progression = [c_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord, a_min_chord, b_dim_chord]

accomp_stream = music21.stream.Part()
bass_clef = music21.clef.BassClef()
accomp_stream.append(bass_clef)


def generate_accompaniment(chord_progression):
    generate_chord_accompaniment(chord_progression)
    return accomp_stream


def generate_chord_accompaniment(chord_progression):
    for chord in chord_progression:
        accomp_stream.append(music21.chord.Chord(c_major_chord_progression[chord - 1]))