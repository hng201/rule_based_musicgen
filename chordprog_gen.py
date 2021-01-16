import random, music21

# Array to store generated chord progression
new_chord_progression = []


def generate_chord_progression():
    #x = random.randint(0, 1)
    x = 0
    if x == 0:
        return generate_major_chord_progression()
    else:
        generate_minor_chord_progression()


# Method to generate new chord progression
# NOTE: current chord progression length is not restricted
def generate_major_chord_progression():
    # Add starting chord for chord progression
    new_chord_progression.append('i')
    # Generate a random number to determine next chord
    i = random.randint(0, 5)
    if i == 0:
        new_chord_progression.append('ii')
    elif i == 1:
        new_chord_progression.append('iii')
    elif i == 2:
        new_chord_progression.append('iv')
    elif i == 3:
        new_chord_progression.append('v')
    elif i == 4:
        new_chord_progression.append('vi')
    elif i == 5:
        new_chord_progression.append('vii_dim')

    x = 1

    # While the last chord is not 'i'
    while new_chord_progression[x] != 'i':
        # If chord at position x is 'iii'
        if new_chord_progression[x] == 'iii':
            # Add chord 'vi' as the next chord
            new_chord_progression.append('vi')
            x += 1
        # If chord at position x is 'vi'
        elif new_chord_progression[x] == 'vi':
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'ii' as the next chord
                new_chord_progression.append('ii')
                x += 1
            else:
                # Add chord 'iv' as the next chord
                new_chord_progression.append('iv')
                x += 1
        # If chord at position x is 'ii' or 'iv'
        elif new_chord_progression[x] == 'ii' or new_chord_progression[x] == 'iv':
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'v' as the next chord
                new_chord_progression.append('v')
                x += 1
            else:
                # Add chord 'vii _dim' as the next chord
                new_chord_progression.append('vii_dim')
                x += 1
                # Generate random number to determine next chord
                num = random.randint(0, 1)
                if num == 0:
                    # Add chord 'i' as the next chord
                    new_chord_progression.append('i')
                    x += 1
                else:
                    # Add chord 'iii' as the next chord
                    new_chord_progression.append('iii')
                    x += 1
        # If chord at position x is 'v'
        elif new_chord_progression[x] == 'v':
            # Add chord 'i' as the next chord
            new_chord_progression.append('i')
            x += 1
        # If chord at position x is 'vii_dim'
        elif new_chord_progression[x] == 'vii_dim':
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'i' as the next chord
                new_chord_progression.append('i')
                x += 1
            else:
                # Add chord 'iii' as the next chord
                new_chord_progression.append('iii')
                x += 1
    # Display the generated chord progression
    print("major: ", new_chord_progression)
    return gmaj_chord_progression(new_chord_progression)


# Adds C Major chord progression notes
def cmaj_chord_progression(chord_progression_structure):
    # Create new stream to store chord progression notes
    chord_prog_stream = music21.stream.Part()
    # Variable to store bass clef value
    bass_clef = music21.clef.BassClef()
    # Add the base clef to the chord progression stream
    chord_prog_stream.append(bass_clef)

    # For each chord in the chord progression structure
    for x in chord_progression_structure:
        # If chord = 'i'
        if x == 'i':
            # Create new chord and assign C major triad notes
            c_maj_chord = music21.chord.Chord(["C3", "E3", "G3"])
            # Set chord duration to semibreve/whole
            c_maj_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(c_maj_chord)
        # If chord = 'ii'
        elif x == 'ii':
            # Create new chord and assign D minor triad notes
            d_min_chord = music21.chord.Chord(["D3", "F3", "A3"])
            # Set chord duration to semibreve/whole
            d_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(d_min_chord)
        # If chord = 'iii'
        elif x == 'iii':
            # Create new chord and assign E minor triad notes
            e_min_chord = music21.chord.Chord(["E3", "G3", "B3"])
            # Set chord duration to semibreve/whole
            e_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(e_min_chord)
        # If chord = 'iv'
        elif x == 'iv':
            # Create new chord and assign F major triad notes
            f_maj_chord = music21.chord.Chord(["F2", "A2", "C3"])
            # Set chord duration to semibreve/whole
            f_maj_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(f_maj_chord)
        # If chord = 'v'
        elif x == 'v':
            # Create new chord and assign G major triad notes
            g_maj_chord = music21.chord.Chord(["G2", "B2", "D3"])
            # Set chord duration to semibreve/whole
            g_maj_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(g_maj_chord)
        # If chord = 'vi'
        elif x == 'vi':
            # Create new chord and assign A minor triad notes
            a_min_chord = music21.chord.Chord(["A2", "C3", "E3"])
            # Set chord duration to semibreve/whole
            a_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(a_min_chord)
        # If chord = 'vii'
        elif x == 'vii_dim':
            # Create new chord and assign B diminished triad notes
            b_dim_chord = music21.chord.Chord(["B2", "D3", "F3"])
            # Set chord duration to semibreve/whole
            b_dim_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(b_dim_chord)
    return chord_prog_stream

def gmaj_chord_progression(chord_progression_structure):
    chord_prog_stream = music21.stream.Part()
    bass_clef = music21.clef.BassClef()
    chord_prog_stream.append(bass_clef)
    key_gmaj = music21.key.KeySignature(1)
    chord_prog_stream.append(key_gmaj)

    for x in chord_progression_structure:
        if x == 'i':
            g_maj_chord = music21.chord.Chord(["G2", "B2", "D3"])
            g_maj_chord.duration.type = "whole"
            chord_prog_stream.append(g_maj_chord)
        elif x == 'ii':
            a_minor_chord = music21.chord.Chord(["A2", "C3", "E3"])
            a_minor_chord.duration.type = "whole"
            chord_prog_stream.append(a_minor_chord)
        elif x == 'iii':
            b_minor_chord = music21.chord.Chord(["B2", "D3", "F#3"])
            b_minor_chord.duration.type = "whole"
            chord_prog_stream.append(b_minor_chord)
        elif x == 'iv':
            c_maj_chord = music21.chord.Chord(["C3", "E3", "G3"])
            c_maj_chord.duration.type = "whole"
            chord_prog_stream.append(c_maj_chord)
        elif x == 'v':
            d_maj_chord = music21.chord.Chord(["D3", "F#3", "A3"])
            d_maj_chord.duration.type = "whole"
            chord_prog_stream.append(d_maj_chord)
        elif x == 'vi':
            e_min_chord = music21.chord.Chord(["E3", "G3", "B3"])
            e_min_chord.duration.type = "whole"
            chord_prog_stream.append(e_min_chord)
        elif x == 'vii_dim':
            fsharp_dim_chord = music21.chord.Chord(["F#2", "A2", "C3"])
            fsharp_dim_chord.duration.type = "whole"
            chord_prog_stream.append(fsharp_dim_chord)
    return chord_prog_stream


def generate_minor_chord_progression():
    new_chord_progression.append('i')

    i = random.randint(0, 6)

    if i == 0:
        new_chord_progression.append('ii_dim')
    elif i == 1:
        new_chord_progression.append('iii')
    elif i == 2:
        new_chord_progression.append('iv')
    elif i == 3:
        new_chord_progression.append('v')
    elif i == 4:
        new_chord_progression.append('vi')
    elif i == 5:
        new_chord_progression.append('vii')
    else:
        new_chord_progression.append('vii_dim')

    x = 1

    while new_chord_progression[x] != 'i':
        num = random.randint(0, 1)
        if new_chord_progression[x] == 'vii':
            new_chord_progression.append('iii')
            x += 1
        elif new_chord_progression[x] == 'iii':
            new_chord_progression.append('vi')
            x += 1
        elif new_chord_progression[x] == 'vi':
            if num == 0:
                new_chord_progression.append('ii_dim')
                x += 1
            else:
                new_chord_progression.append('iv')
                x += 1
        elif new_chord_progression[x] == 'ii_dim':
            if num == 0:
                new_chord_progression.append('v')
                x += 1
            else:
                new_chord_progression.append('vii_dim')
                x += 1
        elif new_chord_progression[x] == 'iv':
            num = random.randint(0, 2)
            if num == 0:
                new_chord_progression.append('v')
                x += 1
            if num == 1:
                new_chord_progression.append('vii_dim')
                x += 1
            else:
                new_chord_progression.append('vii')
                x += 1
        else:
            new_chord_progression.append('i')
            x += 1

    print("Minor: ", new_chord_progression)
    return new_chord_progression

