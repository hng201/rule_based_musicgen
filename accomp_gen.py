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


def generate_accompaniment(chord_progression, key, accomp_rhythm):
    generate_chord_accompaniment(chord_progression, key, accomp_rhythm)
    return accomp_stream


def generate_chord_accompaniment(chord_progression, key, accomp_rhythm):
    if key == 0:
        # Assign chord key to C major chord progression triad chords
        chord_key = c_major_chord_progression
        print("Key: C Major")
    elif key == 1:
        # Create key signature of 1 sharp
        key_signature = music21.key.KeySignature(1)
        # Add key signature to accomp stream
        accomp_stream.append(key_signature)
        # Assign chord_key to G major chord progression triad chords
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
    # Used for position in note_duration to indicate start and end of each bar
    i = 0
    for chord in chord_progression:
        # Used to count duration in bar
        x = 0
        # While there duration does not equal 4
        while x != 4:
            if (chord-1) == len(chord_key):
                # Get chord notes pitch
                chord_notes = select_chord_type(chord_key[chord-2])
                print(chord_notes)
                # Create new chord based off chord from chord progression
                new_chord = music21.chord.Chord(chord_notes)
            else:
                # Get chord notes pitch
                chord_notes = select_chord_type(chord_key[chord - 1])
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
    noteA = ["A", "B"]
    noteB = ["G", "G#", "F", "F#"]
    # Kept as reference
    noteC = ["C", "C#", "D", "E"]
    # sn is starting note
    # Used as reference to ensure other
    # notes are higher pitch than sn
    sn = ""
    if chord[0] in noteA:
        note = chord[0] + "2"
        new_chord.append(note)
        i = 1
        while i != 3:
            num = random.randint(0, 1)
            if num == 0:
                note = chord[i] + "3"
                new_chord.append(note)
            else:
                note = chord[i] + "4"
                new_chord.append(note)
            i += 1
    elif chord in noteB:
        num = random.randint(0, 1)
        if num == 0:
            note = chord[0] + "2"
            sn = note
            new_chord.append(note)
        else:
            note = chord[0] + "3"
            sn = note
            new_chord.append(note)
        if sn [-1] == "2":
            note = chord[1] + "2"
            new_chord.append(note)
            num = random.randint(0, 1)
            if num == 0:
                note = chord[2] + "3"
                new_chord.append(note)
            else:
                note = chord[2] + "4"
                new_chord.append(note)
        else:
            note = chord[1] + "3"
            new_chord.append(note)
            note = chord[2] + "4"
            new_chord.append(note)

    else:
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
            x = 1
            for i in range(2):
                num = random.randint(0, 1)
                if num == 0:
                    note = chord[x] + "3"
                    new_chord.append(note)
                else:
                    note = chord[x] + "4"
                    new_chord.append(note)
                x += 1
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
    return new_chord

