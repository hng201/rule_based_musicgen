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
        # Call method to select a triad note
        current_note = select_triad_note(chord)


def select_triad_note(chord):
    # Variable to store the selected note
    # May be used later for passing note selection
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
