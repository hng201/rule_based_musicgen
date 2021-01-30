import accomp_gen
import chordprog_gen
import music21
import rhythm_gen
import melody_gen
us = music21.environment.UserSettings()
# Set path for software to open music scores
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'

if __name__ == '__main__':
    # Create a new stream
    stream = music21.stream.Stream()
    # Generate a chord progression structure and assign the value to variable chord_progression
    chord_progression, major = chordprog_gen.generate_chord_progression()
    #note_duration = rhythm_gen.generate_note_duration(chord_progression)
    # Generate chord progression and assign the value to variable p_accomp
    #p_accomp, key = accomp_gen.generate_accompaniment(chord_progression, major, note_duration)

    # Generate rhythm for melody
    melody_rhythm = rhythm_gen.generate_note_duration(chord_progression)
    # Generate a melody and assign the value to variable p_melody
    p_melody = melody_gen.generate_melody(chord_progression, melody_rhythm)
    # Add the melody part to the stream
    stream.append(p_melody)
    # Add the accompaniment part to the stream
    #stream.append(p_accomp)
    # Show the stream in MusicXML format
    stream.show()

