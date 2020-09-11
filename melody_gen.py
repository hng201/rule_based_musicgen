import random, music21

melody_stream = music21.stream.Part()
# Variable to store treble clef value
treble_clef = music21.clef.TrebleClef()
# Add the treble clef to the melody stream
melody_stream.append(treble_clef)


# Method to generate melody
def generate_melody(chord_progression):
    # For each chord in the chord progression
    for x in chord_progression:
        # Call method to choose a note
        choose_note(x)
    return melody_stream


# Method to choose notes for each bar
def choose_note(chord):
    # Variable to store current note
    current_note = ""
    # Chooses 4 crochet notes
    for y in range(0, 4):
        if current_note == '':
            # Call method to select a triad note
            current_note = select_triad_note(chord)
        else:
            # Generate a random number between 0 and 1 to decide whether next note is a triad note or a passing note
            num = random.randint(0, 1)
            if num == 0:
                # Call method to select a triad note
                current_note = select_triad_note(chord)
            else:
                # Call method to select a passing note
                select_passing_note(chord, current_note)


def select_triad_note(chord):
    # Variable to store the selected note
    note = ""
    # Variable to store randomly generated number within range of 0 and 2
    num = random.randint(0, 2)
    if chord == 'i':
        if num == 0:
            # Add the note C to the melody stream
            melody_stream.append(music21.note.Note("C"))
            # Set the note value to C
            note = "C"
        if num == 1:
            # Add the note E to the melody stream
            melody_stream.append(music21.note.Note("E"))
            # Set the note value to E
            note = "E"
        if num == 2:
            # Add the note G to the melody stream
            melody_stream.append(music21.note.Note("G"))
            # Set the note value to G
            note = "G"
    if chord == 'ii':
        if num == 0:
            # Add the note D to the melody stream
            melody_stream.append(music21.note.Note("D"))
            # Set the note value to D
            note = "D"
        if num == 1:
            # Add the note F to the melody stream
            melody_stream.append(music21.note.Note("F"))
            # Set the note value to F
            note = "F"
        if num == 2:
            # Add the note A to the melody stream
            melody_stream.append(music21.note.Note("A"))
            # Set the note value to A
            note = "A"
    if chord == 'iii':
        if num == 0:
            # Add the note E to the melody stream
            melody_stream.append(music21.note.Note("E"))
            # Set the note value to E
            note = "E"
        if num == 1:
            # Add the note G to the melody stream
            melody_stream.append(music21.note.Note("G"))
            # Set the note value to G
            note = "G"
        if num == 2:
            # Add the note B to the melody stream
            melody_stream.append(music21.note.Note("B"))
            # Set the note value to B
            note = "B"
    if chord == 'iv':
        if num == 0:
            # Add the note F to the melody stream
            melody_stream.append(music21.note.Note("F"))
            # Set the note value to F
            note = "F"
        if num == 1:
            # Add the note A to the melody stream
            melody_stream.append(music21.note.Note("A"))
            # Set the note value to A
            note = "A"
        if num == 2:
            # Add the note C to the melody stream
            melody_stream.append(music21.note.Note("C"))
            # Set the note value to C
            note = "C"
    if chord == 'v':
        if num == 0:
            # Add the note G to the melody stream
            melody_stream.append(music21.note.Note("G"))
            # Set the note value to G
            note = "G"
        if num == 1:
            # Add the note B to the melody stream
            melody_stream.append(music21.note.Note("B"))
            # Set the note value to B
            note = "B"
        if num == 2:
            # Add the note D to the melody stream
            melody_stream.append(music21.note.Note("D"))
            # Set the note value to D
            note = "D"
    if chord == 'vi':
        if num == 0:
            # Add the note A to the melody stream
            melody_stream.append(music21.note.Note("A"))
            # Set the note value to A
            note = "A"
        if num == 1:
            # Add the note C to the melody stream
            melody_stream.append(music21.note.Note("C"))
            # Set the note value to C
            note = "C"
        if num == 2:
            # Add the note E to the melody stream
            melody_stream.append(music21.note.Note("E"))
            # Set the note value to E
            note = "E"
    if chord == 'vii':
        if num == 0:
            # Add the note B to the melody stream
            melody_stream.append(music21.note.Note("B"))
            # Set the note value to B
            note = "B"
        if num == 1:
            # Add the note D to the melody stream
            melody_stream.append(music21.note.Note("D"))
            # Set the note value to D
            note = "D"
        if num == 2:
            # Add the note F to the melody stream
            melody_stream.append(music21.note.Note("F"))
            # Set the note value to F
            note = "F"
    # Return the value of note
    return note

def select_passing_note(chord, note):
    if chord == 'i':
        # If the note is C
        if note == 'C':
            # Add the passing note D to the melody stream
            melody_stream.append(music21.note.Note("D"))
        # If the note is E
        if note == 'E':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note F to the melody stream
                melody_stream.append(music21.note.Note("F"))
            else:
                # Add the passing note D to the melody stream
                melody_stream.append(music21.note.Note("D"))
        # If the note is G
        if note == 'G':
            # Add the passing note F to the melody stream
            melody_stream.append(music21.note.Note("F"))
    if chord == 'ii':
        # If the note is D
        if note == 'D':
            # Add the passing note E to the melody stream
            melody_stream.append(music21.note.Note("E"))
        # If the note is F
        if note == 'F':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note G to the melody stream
                melody_stream.append(music21.note.Note("G"))
            else:
                # Add the passing note E to the melody stream
                melody_stream.append(music21.note.Note("E"))
        # If the note is A
        if note == 'A':
            # Add the passing note G to the melody stream
            melody_stream.append(music21.note.Note("G"))
    if chord == 'iii':
        # If the note is E
        if note == 'E':
            # Add the passing note F# to the melody stream
            melody_stream.append(music21.note.Note("F#"))
        # If the note is G
        if note == 'G':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note A to the melody stream
                melody_stream.append(music21.note.Note("A"))
            else:
                # Add the passing note F# to the melody stream
                melody_stream.append(music21.note.Note("F#"))
        # If the note is B
        if note == 'B':
            # Add the passing note A to the melody stream
            melody_stream.append(music21.note.Note("A"))
    if chord == 'iv':
        # If the note is F
        if note == 'F':
            # Add the passing note G to the melody stream
            melody_stream.append(music21.note.Note("G"))
        # If the note is A
        if note == 'A':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note Bb to the melody stream
                melody_stream.append(music21.note.Note("B-"))
            else:
                # Add the passing note G to the melody stream
                melody_stream.append(music21.note.Note("G"))
        # If the note is C
        if note == 'C':
            # Add the passing note Bb to the melody stream
            melody_stream.append(music21.note.Note("B-"))
    if chord == 'v':
        # If the note is G
        if note == 'G':
            # Add the passing note A to the melody stream
            melody_stream.append(music21.note.Note("A"))
        # If the note is B
        if note == 'B':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note C to the melody stream
                melody_stream.append(music21.note.Note("C"))
            else:
                # Add the passing note A to the melody stream
                melody_stream.append(music21.note.Note("A"))
        # If the note is D
        if note == 'D':
            # Add the passing note C to the melody stream
            melody_stream.append(music21.note.Note("C"))
    if chord == 'vi':
        # If the note is A
        if note == 'A':
            # Add the passing note B to the melody stream
            melody_stream.append(music21.note.Note("B"))
        # If the note is C
        if note == 'C':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the note D to the melody stream
                melody_stream.append(music21.note.Note("D"))
            else:
                # Add the note B to the melody stream
                melody_stream.append(music21.note.Note("B"))
        # If the note is E
        if note == 'E':
            # Add the note D to the melody stream
            melody_stream.append(music21.note.Note("D"))
    if chord == 'vii':
        # If the note is B
        if note == 'B':
            # Add the note C# to the melody stream
            melody_stream.append(music21.note.Note("C#"))
        # If the note is D
        if note == 'D':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note E to the melody stream
                melody_stream.append(music21.note.Note("E"))
            else:
                # Add the passing note C# to the melody stream
                melody_stream.append(music21.note.Note("C#"))
        # If the note is F
        if note == 'F':
            # Add the passing note E to the melody stream
            melody_stream.append(music21.note.Note("E"))
