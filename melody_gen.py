import random, music21

melody_stream = music21.stream.Part()
# Variable to store treble clef value
treble_clef = music21.clef.TrebleClef()
# Add the treble clef to the melody stream
melody_stream.append(treble_clef)

# Variables to store note pitches for one octave
a = music21.note.Note("A")
a_sharp = music21.note.Note("A#")
a_flat = music21.note.Note("A-")
b = music21.note.Note("B")
b_sharp = music21.note.Note("B#")
b_flat = music21.note.Note("B-")
c = music21.note.Note("C")
c_sharp = music21.note.Note("C#")
c_flat = music21.note.Note("C-")
d = music21.note.Note("D")
d_sharp = music21.note.Note("D#")
d_flat = music21.note.Note("D-")
e = music21.note.Note("E")
e_sharp = music21.note.Note("E#")
e_flat = music21.note.Note("E-")
f = music21.note.Note("F")
f_sharp = music21.note.Note("F#")
f_flat = music21.note.Note("F-")
g = music21.note.Note("G")
g_sharp = music21.note.Note("G#")
g_flat = music21.note.Note("G-")


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
            melody_stream.append(c)
            # Set the note value to C
            note = "C"
        if num == 1:
            # Add the note E to the melody stream
            melody_stream.append(e)
            # Set the note value to E
            note = "E"
        if num == 2:
            # Add the note G to the melody stream
            melody_stream.append(g)
            # Set the note value to G
            note = "G"
    if chord == 'ii':
        if num == 0:
            # Add the note D to the melody stream
            melody_stream.append(d)
            # Set the note value to D
            note = "D"
        if num == 1:
            # Add the note F to the melody stream
            melody_stream.append(f)
            # Set the note value to F
            note = "F"
        if num == 2:
            # Add the note A to the melody stream
            melody_stream.append(a)
            # Set the note value to A
            note = "A"
    if chord == 'iii':
        if num == 0:
            # Add the note E to the melody stream
            melody_stream.append(e)
            # Set the note value to E
            note = "E"
        if num == 1:
            # Add the note G to the melody stream
            melody_stream.append(g)
            # Set the note value to G
            note = "G"
        if num == 2:
            # Add the note B to the melody stream
            melody_stream.append(b)
            # Set the note value to B
            note = "B"
    if chord == 'iv':
        if num == 0:
            # Add the note F to the melody stream
            melody_stream.append(f)
            # Set the note value to F
            note = "F"
        if num == 1:
            # Add the note A to the melody stream
            melody_stream.append(a)
            # Set the note value to A
            note = "A"
        if num == 2:
            # Add the note C to the melody stream
            melody_stream.append(c)
            # Set the note value to C
            note = "C"
    if chord == 'v':
        if num == 0:
            # Add the note G to the melody stream
            melody_stream.append(g)
            # Set the note value to G
            note = "G"
        if num == 1:
            # Add the note B to the melody stream
            melody_stream.append(b)
            # Set the note value to B
            note = "B"
        if num == 2:
            # Add the note D to the melody stream
            melody_stream.append(d)
            # Set the note value to D
            note = "D"
    if chord == 'vi':
        if num == 0:
            # Add the note A to the melody stream
            melody_stream.append(a)
            # Set the note value to A
            note = "A"
        if num == 1:
            # Add the note C to the melody stream
            melody_stream.append(c)
            # Set the note value to C
            note = "C"
        if num == 2:
            # Add the note E to the melody stream
            melody_stream.append(e)
            # Set the note value to E
            note = "E"
    if chord == 'vii':
        if num == 0:
            # Add the note B to the melody stream
            melody_stream.append(b)
            # Set the note value to B
            note = "B"
        if num == 1:
            # Add the note D to the melody stream
            melody_stream.append(d)
            # Set the note value to D
            note = "D"
        if num == 2:
            # Add the note F to the melody stream
            melody_stream.append(f)
            # Set the note value to F
            note = "F"
    # Return the value of note
    return note


def select_passing_note(chord, note):
    if chord == 'i':
        # If the note is C
        if note == 'C':
            # Add the passing note D to the melody stream
            melody_stream.append(d)
        # If the note is E
        if note == 'E':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note F to the melody stream
                melody_stream.append(f)
            else:
                # Add the passing note D to the melody stream
                melody_stream.append(d)
        # If the note is G
        if note == 'G':
            # Add the passing note F to the melody stream
            melody_stream.append(f)
    if chord == 'ii':
        # If the note is D
        if note == 'D':
            # Add the passing note E to the melody stream
            melody_stream.append(e)
        # If the note is F
        if note == 'F':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note G to the melody stream
                melody_stream.append(g)
            else:
                # Add the passing note E to the melody stream
                melody_stream.append(e)
        # If the note is A
        if note == 'A':
            # Add the passing note G to the melody stream
            melody_stream.append(g)
    if chord == 'iii':
        # If the note is E
        if note == 'E':
            # Add the passing note F# to the melody stream
            melody_stream.append(f_sharp)
        # If the note is G
        if note == 'G':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note A to the melody stream
                melody_stream.append(a)
            else:
                # Add the passing note F# to the melody stream
                melody_stream.append(f_sharp)
        # If the note is B
        if note == 'B':
            # Add the passing note A to the melody stream
            melody_stream.append(a)
    if chord == 'iv':
        # If the note is F
        if note == 'F':
            # Add the passing note G to the melody stream
            melody_stream.append(g)
        # If the note is A
        if note == 'A':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note Bb to the melody stream
                melody_stream.append(b_flat)
            else:
                # Add the passing note G to the melody stream
                melody_stream.append(g)
        # If the note is C
        if note == 'C':
            # Add the passing note Bb to the melody stream
            melody_stream.append(b_flat)
    if chord == 'v':
        # If the note is G
        if note == 'G':
            # Add the passing note A to the melody stream
            melody_stream.append(a)
        # If the note is B
        if note == 'B':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note C to the melody stream
                melody_stream.append(c)
            else:
                # Add the passing note A to the melody stream
                melody_stream.append(a)
        # If the note is D
        if note == 'D':
            # Add the passing note C to the melody stream
            melody_stream.append(c)
    if chord == 'vi':
        # If the note is A
        if note == 'A':
            # Add the passing note B to the melody stream
            melody_stream.append(b)
        # If the note is C
        if note == 'C':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the note D to the melody stream
                melody_stream.append(d)
            else:
                # Add the note B to the melody stream
                melody_stream.append(b)
        # If the note is E
        if note == 'E':
            # Add the note D to the melody stream
            melody_stream.append(d)
    if chord == 'vii':
        # If the note is B
        if note == 'B':
            # Add the note C# to the melody stream
            melody_stream.append(c_sharp)
        # If the note is D
        if note == 'D':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                # Add the passing note E to the melody stream
                melody_stream.append(e)
            else:
                # Add the passing note C# to the melody stream
                melody_stream.append(c_sharp)
        # If the note is F
        if note == 'F':
            # Add the passing note E to the melody stream
            melody_stream.append(e)
