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
    passing_note = False
    # Chooses 4 crochet notes
    for y in range(0, 4):
        if current_note == '' or y == 3 or passing_note is True:
            # Call method to select a triad note
            current_note, passing_note = select_triad_note(chord, current_note, passing_note)
            print(y)
        else:
            # Generate a random number between 0 and 1 to decide whether next note is a triad note or a passing note
            num = random.randint(0, 1)
            if num == 0:
                # Call method to select a triad note
                current_note, passing_note = select_triad_note(chord, current_note, passing_note)
                print(y)
            if num == 1:
                # Call method to select a passing note
                current_note, passing_note = select_passing_note(chord, current_note)
                print(y)


def select_triad_note(chord, current_note, passing_note):
    # Variable to store the selected note
    note = ''
    # Variable to store note to add
    new_note = ''
    if current_note == '' or passing_note is False:
        # Variable to store randomly generated number within range of 0 and 2
        num = random.randint(0, 2)
        if chord == 'i':
            if num == 0:
                new_note = music21.note.Note("C")
                # Set the note value to C
                note = "C"
            if num == 1:
                new_note = music21.note.Note("E")
                # Set the note value to E
                note = "E"
            if num == 2:
                new_note = music21.note.Note("G")
                # Set the note value to G
                note = "G"
        if chord == 'ii':
            if num == 0:
                new_note = music21.note.Note("D")
                # Set the note value to D
                note = "D"
            if num == 1:
                new_note = music21.note.Note("F")
                # Set the note value to F
                note = "F"
            if num == 2:
                new_note = music21.note.Note("A")
                # Set the note value to A
                note = "A"
        if chord == 'iii':
            if num == 0:
                new_note = music21.note.Note("E")
                # Set the note value to E
                note = "E"
            if num == 1:
                new_note = music21.note.Note("G")
                # Set the note value to G
                note = "G"
            if num == 2:
                new_note = music21.note.Note("B")
                # Set the note value to B
                note = "B"
        if chord == 'iv':
            if num == 0:
                new_note = music21.note.Note("F")
                # Set the note value to F
                note = "F"
            if num == 1:
                new_note = music21.note.Note("A")
                # Set the note value to A
                note = "A"
            if num == 2:
                new_note = music21.note.Note("C")
                # Set the note value to C
                note = "C"
        if chord == 'v':
            if num == 0:
                new_note = music21.note.Note("G")
                # Set the note value to G
                note = "G"
            if num == 1:
                new_note = music21.note.Note("B")
                # Set the note value to B
                note = "B"
            if num == 2:
                new_note = music21.note.Note("D")
                # Set the note value to D
                note = "D"
        if chord == 'vi':
            if num == 0:
                new_note = music21.note.Note("A")
                # Set the note value to A
                note = "A"
            if num == 1:
                new_note = music21.note.Note("C")
                # Set the note value to C
                note = "C"
            if num == 2:
                new_note = music21.note.Note("E")
                # Set the note value to E
                note = "E"
        if chord == 'vii':
            if num == 0:
                new_note = music21.note.Note("B")
                # Set the note value to B
                note = "B"
            if num == 1:
                new_note = music21.note.Note("D")
                # Set the note value to D
                note = "D"
            if num == 2:
                new_note = music21.note.Note("F")
                # Set the note value to F
                note = "F"
    else:
        if chord == 'i':
            if current_note == 'D':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("C")
                    note = "C"
                else:
                    new_note = music21.note.Note("E")
                    note = "E"
            if current_note == 'F':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("E")
                    note = "E"
                else:
                    new_note = music21.note.Note("G")
                    note = "G"
        if chord == 'ii':
            if current_note == 'E':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("D")
                    note = "D"
                else:
                    new_note = music21.note.Note("F")
                    note = "F"
            if current_note == 'G':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("F")
                    note = "F"
                else:
                    new_note = music21.note.Note("A")
                    note = "A"
        if chord == 'iii':
            if current_note == 'F#':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("E")
                    note = "E"
                else:
                    new_note = music21.note.Note("G")
                    note = "G"
            if current_note == 'A':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("G")
                    note = "G"
                else:
                    new_note = music21.note.Note("B")
                    note = "B"
        if chord == 'iv':
            if current_note == 'G':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("F")
                    note = "F"
                else:
                    new_note = music21.note.Note("A")
                    note = "A"
            if current_note == "Bb":
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("A")
                    note = "A"
                else:
                    new_note = music21.note.Note("C")
                    note = "C"
        if chord == 'v':
            if current_note == 'A':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("G")
                    note = "G"
                else:
                    new_note = music21.note.Note("B")
                    note = "B"
            if current_note == 'C':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("B")
                    note = "B"
                else:
                    new_note = music21.note.Note("D")
                    note = "D"
        if chord == 'vi':
            if current_note == 'B':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("A")
                    note = "A"
                else:
                    new_note = music21.note.Note("C")
                    note = "C"
            if current_note == 'D':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("C")
                    note = "C"
                else:
                    new_note = music21.note.Note("E")
                    note = "E"
        if chord == 'vii':
            if current_note == "C#":
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("B")
                    note = "B"
                else:
                    new_note = music21.note.Note("D")
                    note = "D"
            if current_note == 'E':
                num = random.randint(0, 1)
                if num == 0:
                    new_note = music21.note.Note("D")
                    note = "D"
                else:
                    new_note = music21.note.Note("F")
                    note = "F"
    melody_stream.append(new_note)
    print(note + " triad note")
    passing_note = False
    return note, passing_note


def select_passing_note(chord, current_note):
    note = ''
    new_note = ''
    if chord == 'i':
        # If the note is C
        if current_note == 'C':
            new_note = music21.note.Note("D")
            note = "D"
        # If the note is E
        if current_note == 'E':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("F")
                note = "F"
            else:
                new_note = music21.note.Note("D")
                note = "D"
        # If the note is G
        if current_note == 'G':
            new_note = music21.note.Note("F")
            note = "F"
    if chord == 'ii':
        # If the note is D
        if current_note == 'D':
            new_note = music21.note.Note("E")
            note = "E"
        # If the note is F
        if current_note == 'F':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("G")
                note = "G"
            else:
                new_note = music21.note.Note("E")
                note = "E"
        # If the note is A
        if current_note == 'A':
            new_note = music21.note.Note("G")
            note = "G"
    if chord == 'iii':
        # If the note is E
        if current_note == 'E':
            new_note = music21.note.Note("F#")
            note = "F#"
        # If the note is G
        if current_note == 'G':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("A")
                note = "A"
            else:
                # Add the passing note F# to the melody stream
                new_note = music21.note.Note("F#")
                note = "F#"
        # If the note is B
        if current_note == 'B':
            new_note = music21.note.Note("A")
            note = "A"
    if chord == 'iv':
        # If the note is F
        if current_note == 'F':
            new_note = music21.note.Note("G")
            note = "G"
        # If the note is A
        if current_note == 'A':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("B-")
                note = "Bb"
            else:
                new_note = music21.note.Note("G")
                note = "G"
        # If the note is C
        if current_note == 'C':
            new_note = music21.note.Note("B-")
            note = "Bb"
    if chord == 'v':
        # If the note is G
        if current_note == 'G':
            new_note = music21.note.Note("A")
            note = "A"
        # If the note is B
        if current_note == 'B':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("C")
                note = "C"
            else:
                new_note = music21.note.Note("A")
                note = "A"
        # If the note is D
        if current_note == 'D':
            new_note = music21.note.Note("C")
            note = "C"
    if chord == 'vi':
        # If the note is A
        if current_note == 'A':
            new_note = music21.note.Note("B")
            note = "B"
        # If the note is C
        if current_note == 'C':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("D")
                note = "D"
            else:
                new_note = music21.note.Note("B")
                note = "B"
        # If the note is E
        if current_note == 'E':
            new_note = music21.note.Note("D")
            note = "D"
    if chord == 'vii':
        # If the note is B
        if current_note == 'B':
            new_note = music21.note.Note("C#")
            note = "C#"
        # If the note is D
        if current_note == 'D':
            # Generate a random number between 0 and 1 to decide which passing note to use
            num = random.randint(0, 1)
            if num == 0:
                new_note = music21.note.Note("E")
                note = "E"
            else:
                new_note = music21.note.Note("C#")
                note = "C#"
        # If the note is F
        if current_note == 'F':
            # Add the passing note E to the melody stream
            new_note = music21.note.Note("E")
            note = "E"
    melody_stream.append(new_note)
    print(note + " passing note")
    passing_note = True
    return note, passing_note
