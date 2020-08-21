import music21
import chordprog_gen

us = music21.environment.UserSettings()
# Set path for software to open music scores
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'

if __name__ == '__main__':
    chordprog_gen.generate_chord_progression()

