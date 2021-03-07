import music21
import random

c_maj_chord = ["C", "E", "G"]
csharp_min_chord = ["C#", "E", "G#"]
csharp_dim_chord = ["C#", "E", "G"]

d_maj_chord = ["D", "F#", "A"]
d_min_chord = ["D", "F", "A"]

e_maj_chord = ["E", "G#", "B"]
e_min_chord = ["E", "G", "B"]

f_maj_chord = ["F", "A", "C"]
fsharp_min_chord = ["F#", "A", "C#"]
fsharp_dim_chord = ["F#", "A", "C"]

g_maj_chord = ["G", "B", "D"]
gsharp_dim_chord = ["G#", "B", "D"]

a_maj_chord = ["A", "C#", "E"]
a_min_chord = ["A", "C", "E"]

b_min_chord = ["B", "D", "F#"]
b_dim_chord = ["B", "D", "F"]

c_major_chord_progression = [c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord, a_min_chord, b_dim_chord]
g_major_chord_progression = [g_maj_chord, a_min_chord, b_min_chord, c_maj_chord, d_maj_chord, e_min_chord,
                             fsharp_dim_chord]
d_major_chord_progression = [d_maj_chord, e_min_chord, fsharp_min_chord, g_maj_chord, a_maj_chord, b_min_chord,
                             csharp_dim_chord]
a_major_chord_progression = [a_maj_chord, b_min_chord, csharp_min_chord, d_maj_chord, e_maj_chord, fsharp_min_chord,
                             gsharp_dim_chord]

a_minor_chord_progression = [a_min_chord, b_dim_chord, c_maj_chord, d_min_chord, e_min_chord, f_maj_chord, g_maj_chord]
e_minor_chord_progression = [e_min_chord, fsharp_dim_chord, g_maj_chord, a_min_chord, b_min_chord, c_maj_chord,
                             d_maj_chord]
b_minor_chord_progression = [b_min_chord, csharp_dim_chord, d_maj_chord, e_min_chord, fsharp_min_chord, g_maj_chord,
                             a_maj_chord]
fsharp_minor_chord_progression = [fsharp_min_chord, gsharp_dim_chord, a_maj_chord, b_min_chord, csharp_min_chord,
                                  d_maj_chord, e_maj_chord]

accomp_stream = music21.stream.Part()
bass_clef = music21.clef.BassClef()
accomp_stream.append(bass_clef)


def generate_accompaniment(chord_progression, key, accomp_rhythm, rest_limit, accomp_type):
    accomp_key = get_accomp_key(key)
    if accomp_type == 0:
        for chord in chord_progression:
            generate_chord_accompaniment(chord, accomp_key, accomp_rhythm, rest_limit)
    elif accomp_type == 1:
        for chord in chord_progression:
            generate_arpeggio_accomp(chord, accomp_key)
    else:
        for chord in chord_progression:
            num = random.randint(0, 1)
            if num == 0:
                generate_chord_accompaniment(chord, accomp_key, accomp_rhythm, rest_limit)
            else:
                generate_arpeggio_accomp(chord, accomp_key)
    return accomp_stream


def get_accomp_key(key):
    if key == 0:
        # Assign chord key to C major chord progression triad chords
        chord_key = c_major_chord_progression
        print("Key: C Major")
    elif key == 1:
        # Create key signature of 1 sharp
        key_signature = music21.key.KeySignature(1)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign accomp_key to G major chord progression triad chords
        chord_key = g_major_chord_progression
        print("Key: G Major")
    elif key == 2:
        # Create key signature of 2 sharps
        key_signature = music21.key.KeySignature(2)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord key to D major chord progression triad chords
        chord_key = d_major_chord_progression
        print("Key: D Major")
    elif key == 3:
        # Create key signature of 3 sharps
        key_signature = music21.key.KeySignature(3)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord key to A major chord progression triad chords
        chord_key = a_major_chord_progression
        print("Key: A Major")
    elif key == 4:
        # Assign chord key to A minor chord progression triad chords
        chord_key = a_minor_chord_progression
        print("Key: A Minor")
    elif key == 5:
        # Create key signature of 1 sharp
        key_signature = music21.key.KeySignature(1)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord key to E minor chord progression triad chords
        chord_key = e_minor_chord_progression
        print("Key: E Minor")
    elif key == 6:
        # Create key signature of 2 sharps
        key_signature = music21.key.KeySignature(2)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord key to B minor chord progression triad chords
        chord_key = b_minor_chord_progression
        print("Key: B Minor")
    else:
        # Create key signature of 3 sharps
        key_signature = music21.key.KeySignature(3)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord key to F# minor chord progression triad chords
        chord_key = fsharp_minor_chord_progression
        print("Key: F# Minor")
    return chord_key


def generate_chord_accompaniment(chord, accomp_key, accomp_rhythm, rest_limit):
    # Counter for rhythm
    i = 0
    # Used to count duration in bar
    x = 0
    # Count for total rest duration per bar
    rest_count = 0
    # While there duration does not equal 4
    while x != 4:
        # Generate random number to decide between chord note and rest note
        num = random.randint(0, 1)
        # If num is 0 or rest_count plus current note duration is less than rest_limit
        if num == 0 and rest_count + accomp_rhythm[i].quarterLength < rest_limit:
            # Create new rest note
            rest = music21.note.Rest()
            # Assign rest the note duration
            rest.duration = accomp_rhythm[i]
            # Add the rest to the stream
            accomp_stream.append(rest)
            # Add note duration to rest_count
            rest_count = rest_count + accomp_rhythm[i].quarterLength
            # Add the note duration used to current duration in bar
            x = x + accomp_rhythm[i].quarterLength
        else:
            if (chord-1) == len(accomp_key):
                # Get chord notes pitch
                chord_notes = select_chord_type(accomp_key[chord - 2])
                # Print chord notes for testing purposes
                print(chord_notes)
                # Create new chord based off chord from chord progression
                new_chord = music21.chord.Chord(chord_notes)
            else:
                # Get chord notes pitch
                chord_notes = select_chord_type(accomp_key[chord - 1])
                # Print chord notes for testing purposes
                print(chord_notes)
                # Create new chord based off chord from chord progression
                new_chord = music21.chord.Chord(chord_notes)
            # Assign the chord the note duration
            new_chord.duration = accomp_rhythm[i]
            # Add the new chord to the stream
            accomp_stream.append(new_chord)
            # Add note duration used to current duration in bar
            x = x + accomp_rhythm[i].quarterLength
        # Increment position
        i += 1


def generate_arpeggio_accomp(chord, accomp_key):
    x = 0
    noteA = ["F", "F#", "G", "G#"]
    noteB = ["A", "B"]
    while x != 4:
        num = random.randint(0, 2)
        if num == 0:
            num = random.randint(0, 2)
            if (chord-1) == len(accomp_key):
                # If num is 0, Add single arpeggio in ascending manner
                if num == 0:
                    # Get chord notes
                    chord_notes = accomp_key[chord - 2]
                    # Print chord notes for testing purposes
                    print(chord_notes)
                    pitch = random.randint(1, 4)
                    for note in chord_notes:
                        new_note = music21.note.Note(note + str(pitch))
                        new_note.duration = music21.duration.Duration('eighth')
                        if x + new_note.duration.quarterLength <= 4:
                            accomp_stream.append(new_note)
                            x = x + new_note.duration.quarterLength
                # If num is 1, Add ascending arpeggio
                elif num == 1:
                    # Get chord notes
                    chord_notes = accomp_key[chord - 2]
                    # Print chord notes for testing purposes
                    print(chord_notes)
                    y = 1
                    for note in chord_notes:
                        new_note = music21.note.Note(note + str(y))
                        new_note.duration = music21.duration.Duration('eighth')
                        if x + new_note.duration.quarterLength <= 4:
                            accomp_stream.append(new_note)
                            x = x + new_note.duration.quarterLength
                    y += 1
                # Add descending arpeggio
                else:
                    # Get chord notes pitch
                    chord_notes = accomp_key[chord - 2]
                    new_chord = [chord_notes[0], chord_notes[2], chord_notes[1]]
                    # Print new chord for testing purposes
                    print(new_chord)
                    y = 4
                    if new_chord[0] in noteA:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                                if new_note == new_chord[1]:
                                    y -= 1
                    elif new_chord[0] in noteB:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                        y -= 1
                    else:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                                if note == chord_notes[0]:
                                    y -= 1
            else:
                # If num = 0, add single arpeggio
                if num == 0:
                    # Get chord notes
                    chord_notes = accomp_key[chord - 1]
                    # Print chord notes for testing purposes
                    print(chord_notes)
                    pitch = random.randint(1, 4)
                    for note in chord_notes:
                        new_note = music21.note.Note(note + str(pitch))
                        new_note.duration = music21.duration.Duration('eighth')
                        if x + new_note.duration.quarterLength <= 4:
                            accomp_stream.append(new_note)
                            x = x + new_note.duration.quarterLength
                # If num is 1, add ascending arpeggio
                elif num == 1:
                    # Get chord notes
                    chord_notes = accomp_key[chord - 2]
                    # Print chord notes for testing purposes
                    print(chord_notes)
                    y = 1
                    for note in chord_notes:
                        new_note = music21.note.Note(note + str(y))
                        new_note.duration = music21.duration.Duration('eighth')
                        if x + new_note.duration.quarterLength <= 4:
                            accomp_stream.append(new_note)
                            x = x + new_note.duration.quarterLength
                    y += 1
                # Add descending arpeggio
                else:
                    # Get chord notes
                    chord_notes = accomp_key[chord - 1]
                    new_chord = [chord_notes[0], chord_notes[2], chord_notes[1]]
                    # Print new chord for testing purposes
                    print(new_chord)
                    y = 4
                    if new_chord[0] in noteA:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                                if note == new_chord[1]:
                                    y -= 1
                    elif new_chord[0] in noteB:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                        y -= 1
                    else:
                        for note in new_chord:
                            new_note = music21.note.Note(note + str(y))
                            new_note.duration = music21.duration.Duration('eighth')
                            if x + new_note.duration.quarterLength <= 4:
                                accomp_stream.append(new_note)
                                x = x + new_note.duration.quarterLength
                                if note == new_chord[0]:
                                    y -= 1
        elif num == 1:
            if (chord-1) == len(accomp_key):
                # Get chord notes pitch
                chord_notes = select_chord_type(accomp_key[chord - 2])
                # Print chord notes for testing purposes
                print(chord_notes)
                for note in chord_notes:
                    new_note = music21.note.Note(note)
                    new_note.duration = music21.duration.Duration('eighth')
                    if x + new_note.duration.quarterLength <= 4:
                        accomp_stream.append(new_note)
                        x = x + new_note.duration.quarterLength
            else:
                # Get chord notes pitch
                chord_notes = select_chord_type(accomp_key[chord - 1])
                # Print chord notes for testing purposes
                print(chord_notes)
                for note in chord_notes:
                    new_note = music21.note.Note(note)
                    new_note.duration = music21.duration.Duration('eighth')
                    if x + new_note.duration.quarterLength <= 4:
                        accomp_stream.append(new_note)
                        x = x + new_note.duration.quarterLength
        else:
            rest = music21.note.Rest()
            if 4 - x >= 2:
                num = random.randint(0, 2)
                if num == 0:
                    rest.duration = music21.duration.Duration('eighth')
                elif num == 1:
                    rest.duration = music21.duration.Duration('quarter')
                else:
                    rest.duration = music21.duration.Duration('half')
            elif 4 - x >= 1:
                num = random.randint(0, 1)
                if num == 0:
                    rest.duration = music21.duration.Duration('eighth')
                else:
                    rest.duration = music21.duration.Duration('quarter')
            else:
                rest.duration = music21.duration.Duration('eighth')
            accomp_stream.append(rest)
            x = x + rest.duration.quarterLength


def select_chord_type(chord):
    # Array to store new order of chord notes
    chord_type = []
    num = random.randint(0, 2)
    if num == 0:
        # Chord type is root
        chord_type = chord
    elif num == 1:
        # Chord type is 1st inversion
        chord_type.append(chord[1])
        chord_type.append(chord[2])
        chord_type.append(chord[0])
    else:
        # Chord type is 2nd inversion
        chord_type.append(chord[2])
        chord_type.append(chord[0])
        chord_type.append(chord[1])
    return select_chord_pitch(chord_type)


def select_chord_pitch(chord):
    # New array to store chord notes with pitches
    new_chord = []
    # List of arrays for notes
    # This effects pitch range to ensure notes
    # are still in correct order for chord type
    noteA = ["A", "B", "E"]
    noteB = ["F", "F#"]
    noteC = ["C", "C#", "D"]
    # Kept as reference
    noteD = ["G", "G#"]
    # sn is starting note
    # Used as reference to ensure other
    # notes are higher pitch than sn
    sn = ""
    if chord[0] in noteA:
        note = chord[0] + "2"
        new_chord.append(note)
        if chord[0] == "E" or "E#":
            note = chord[0] + "3"
            new_chord.append(note)
            note = chord[0] + "4"
            new_chord.append(note)
        else:
            num = random.randint(0, 1)
            if num == 0:
                note = chord[1] + "3"
                new_chord.append(note)
            else:
                note = chord[1] + "4"
                new_chord.append(note)
            note = chord[2] + "4"
            new_chord.append(note)
    elif chord[0] in noteB:
        num = random.randint(0, 1)
        if num == 0:
            note = chord[0] + "2"
            sn = note
            new_chord.append(note)
        else:
            note = chord[0] + "3"
            sn = note
            new_chord.append(note)
        if sn[-1] == "2":
            note = chord[1] + "2"
            new_chord.append(note)
            num = random.randint(0, 1)
            if num == 0:
                note = chord[2] + "3"
                new_chord.append(note)
            else:
                note = chord[2] + "4"
                new_chord.append(note)
        elif sn[-1] == "3":
            note = chord[1] + "3"
            new_chord.append(note)
            note = chord[2] + "4"
            new_chord.append(note)
        else:
            note = chord[1] + "4"
            new_chord.append(note)
            note = chord[2] + "5"
            new_chord.append(note)
    elif chord[0] in noteC:
        num = random.randint(0, 2)
        if num == 0:
            note = chord[0] + "2"
            sn = note
            new_chord.append(note)
        elif num == 1:
            note = chord[0] + "3"
            sn = note
            new_chord.append(note)
        elif num == 2:
            note = chord[0] + "4"
            sn = note
            new_chord.append(note)
        if sn[-1] == "4":
            x = 1
            for i in range(2):
                note = chord[x] + "4"
                new_chord.append(note)
                x += 1
        elif sn[-1] == "3":
            note = chord[1] + "3"
            new_chord.append(note)
            num = random.randint(0, 1)
            if num == 0:
                note = chord[2] + "3"
                new_chord.append(note)
            else:
                note = chord[2] + "4"
                new_chord.append(note)
        elif sn[-1] == "2":
            x = 1
            for i in range(2):
                num = random.randint(0, 2)
                if len(new_chord) == 2:
                    temp = new_chord[1]
                    if temp[-1] == "2":
                        if num == 0:
                            note = chord[x] + "2"
                            new_chord.append(note)
                        elif num == 1:
                            note = chord[x] + "3"
                            new_chord.append(note)
                        else:
                            note = chord[x] + "4"
                            new_chord.append(note)
                        x += 1
                    elif temp[-1] == "3":
                        num = random.randint(0, 1)
                        if num == 0:
                            note = chord[x] + "3"
                            new_chord.append(note)
                        else:
                            note = chord[x] + "4"
                            new_chord.append(note)
                        x += 1
                    else:
                        note = chord[x] + "4"
                        new_chord.append(note)
                    x += 1
                else:
                    if num == 0:
                        note = chord[x] + "2"
                        new_chord.append(note)
                    elif num == 1:
                        note = chord[x] + "3"
                        new_chord.append(note)
                    else:
                        note = chord[x] + "4"
                        new_chord.append(note)
                    x += 1
    else:
        num = random.randint(0, 1)
        if num == 0:
            note = chord[0] + "2"
            new_chord.append(note)
            if chord[1] == "B":
                note = chord[1] + "2"
                new_chord.append(note)
            else:
                note = chord[1] + "3"
                new_chord.append(note)
            note = chord[2] + "3"
            new_chord.append(note)
        else:
            note = chord[0] + "3"
            new_chord.append(note)
            if chord[1] == "B":
                note = chord[1] + "3"
                new_chord.append(note)
            else:
                note = chord[1] + "4"
                new_chord.append(note)
            note = chord[2] + "4"
            new_chord.append(note)
    return new_chord
