import music21, chordprog_gen, melody_gen

us = music21.environment.UserSettings()
# Set path for software to open music scores
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'

if __name__ == '__main__':
    stream = music21.stream.Stream()
    chord_progression = []
    chord_progression = chordprog_gen.generate_chord_progression()
    p_accomp = chordprog_gen.cmaj_chord_progression(chord_progression)
    p_melody = melody_gen.generate_melody(chord_progression)
    stream.append(p_melody)
    stream.append(p_accomp)
    stream.show()

