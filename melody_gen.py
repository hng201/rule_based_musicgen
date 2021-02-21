import music21
import random

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
def generate_melody(chord_progression, melody_rhythm, key, rest_limit):
    if key == 0:
        # Assign notes to C major notes
        notes = c_major_notes
    elif key == 1:
        # Create key signature of 1 sharp
        key_signature = music21.key.KeySignature(1)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assign notes to G major notes
        notes = g_major_notes
    elif key == 2:
        # Create key signature of 2 sharps
        key_signature = music21.key.KeySignature(2)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assign notes to D major notes
        notes = d_major_notes
    elif key == 3:
        # Create key signature of 3 sharps
        key_signature = music21.key.KeySignature(3)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assign notes to A major notes
        notes = a_major_notes
    elif key == 4:
        # Assign notes to A minor notes
        notes = a_minor_notes
    elif key == 5:
        # Create key signature of 1 sharp
        key_signature = music21.key.KeySignature(1)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assign notes to E minor notes
        notes = e_minor_notes
    elif key == 6:
        # Create key signature of 2 sharps
        key_signature = music21.key.KeySignature(2)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assign notes to B minor notes
        notes = b_minor_notes
    else:
        # Create key signature of 3 sharps
        key_signature = music21.key.KeySignature(3)
        # Add key signature to melody stream
        melody_stream.append(key_signature)
        # Assigns notes to F# minor notes
        notes = fsharp_minor_notes
    # Choose note based on chord progression, melody rhythm and notes and rest limit
    choose_note(chord_progression, melody_rhythm, notes, rest_limit)
    return melody_stream


def choose_note(chord_progression, melody_rhythm, notes, rest_limit):
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
            num = random.randint(0, 1)
            if num == 0 and rest_limit - melody_rhythm[i].quarterLength >=0:
                # Create new rest note
                rest = music21.note.Rest()
                # Assign note duration to rest
                rest.duration = melody_rhythm[i]
                # Add rest to melody stream
                melody_stream.append(rest)
                # Take away note duration used from rest limit
                rest_limit = rest_limit - melody_rhythm[i].quarterLength
                # Add note duration used to current note duration in bar
                x = x + melody_rhythm[i].quarterLength
            else:
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
