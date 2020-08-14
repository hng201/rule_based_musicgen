# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import music21

us = music21.environment.UserSettings()
# Set path for software to open music scores
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'


def display_chord():
    # create a new stream to store notes
    stream1 = music21.stream.Stream()
    stream1.append(music21.chord.Chord(['C', 'E', 'G']))
    stream1.show()


if __name__ == '__main__':
    display_chord()

