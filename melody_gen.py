import random, music21

c_major_notes = ["C", "D", "E", "F", "G", "A", "B"]
g_major_notes = ["G", "A", "B", "C", "D", "E", "F#"]
d_major_notes = ["D", "E", "F#", "G", "A", "B", "C#"]
a_major_notes = ["A", "B", "C#", "D", "E", "F#", "G#"]

a_minor_notes = ["A", "B", "C", "D", "E", "F", "G"]
e_minor_notes = ["E", "F#", "G", "A", "B", "C", "D"]
b_minor_notes = ["B", "C#", "D", "E", "F#", "G", "A"]
fsharp_minor_notes = ["F#", "G#", "A", "B", "C#", "D", "E"]


melody_stream = music21.stream.Part()
# Variable to store treble clef value
treble_clef = music21.clef.TrebleClef()
# Add the treble clef to the melody stream
melody_stream.append(treble_clef)


# Method to generate melody
def generate_melody(chord_progression, melody_rhythm, major, key):
    if major:
        if key == 0:
            notes = c_major_notes
        elif key == 1:
            key_signature = music21.key.KeySignature(1)
            melody_stream.append(key_signature)
            notes = g_major_notes
        elif key == 2:
            key_signature = music21.key.KeySignature(2)
            melody_stream.append(key_signature)
            notes = d_major_notes
        else:
            key_signature = music21.key.KeySignature(3)
            melody_stream.append(key_signature)
            notes = a_major_notes
    else:
        if key == 0:
            notes = a_minor_notes
        elif key == 1:
            key_signature = music21.key.KeySignature(1)
            melody_stream.append(key_signature)
            notes = e_minor_notes
        elif key == 2:
            key_signature = music21.key.KeySignature(2)
            melody_stream.append(key_signature)
            notes = b_minor_notes
        else:
            key_signature = music21.key.KeySignature(3)
            melody_stream.append(key_signature)
            notes = fsharp_minor_notes
    choose_note(chord_progression, melody_rhythm, notes)
    return melody_stream


def choose_note(chord_progression, melody_rhythm, notes):
    # Used to store current note value
    current_note = 0
    # Counter for rhythm
    i = 0

    for chord in chord_progression:
        # Count duration used for bar
        x = 0
        # Define position for notes based on chord
        note_choices = [chord - 1, chord, chord + 1, chord + 2, chord + 3]
        # Current duration does not equal 4
        while x != 4:
            # If note is the first note of a new bar
            if x == 0:
                # Select a random triad note
                note = random.choice([chord - 1, chord + 1, chord + 3])
                # If the note value is greater than 6
                if note > 6:
                    # Minus 6 to get the note value
                    # This is to ensure note value is not out of bound of array
                    note = note - 6
                # Create a new note
                new_note = music21.note.Note(notes[note])
                # Assign the new note a duration
                new_note.duration = melody_rhythm[i]
                # Add note to melody stream
                melody_stream.append(new_note)
                # Assign current note to note value
                current_note = note
                # Add note duration used to current note duration in bar
                x = x + melody_rhythm[i].quarterLength
                # Increment position
                i += 1
            # If the current note value is odd/ is a passing note
            elif current_note % 2 > 0:
                # Select a note above or below the current note
                note = random.choice([current_note - 1, current_note + 1])
                # If note value is greater than 6
                if note > 6:
                    # Minus 6 to get note value
                    note = note - 6
                # Create new note
                new_note = music21.note.Note(notes[note])
                # Assign new note a duration
                new_note.duration = melody_rhythm[i]
                # Add new note to melody stream
                melody_stream.append(new_note)
                # Assign current note to note value
                current_note = note
                # Add note duration used to current note duration in bar
                x = x + melody_rhythm[i].quarterLength
                # Increment position
                i += 1
            else:
                # Select a random note
                note = random.choice(note_choices)
                # If note value is greater than 6
                if note > 6:
                    # Minus 6 to get note value
                    note = note - 6
                # Create new note
                new_note = music21.note.Note(notes[note])
                # Assign new note a duration
                new_note.duration = melody_rhythm[i]
                # Add new note to melody stream
                melody_stream.append(new_note)
                # Assign current note to note value
                current_note = note
                # Add note duration used to current note duration in bar
                x = x + melody_rhythm[i].quarterLength
                # Increment position
                i += 1

