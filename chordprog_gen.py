import random, music21

# Array to store generated chord progression
new_chord_progression = []


# Method to generate new chord progression
# NOTE: current chord progression length is not restricted
def generate_chord_progression():
    # Add starting chord for chord progression
    new_chord_progression.append('i')
    # Generate a random number to determine next chord
    i = random.randint(0, 4)
    if i == 0:
        new_chord_progression.append('ii')
    if i == 1:
        new_chord_progression.append('iii')
    if i == 2:
        new_chord_progression.append('iv')
    if i == 3:
        new_chord_progression.append('v')
    if i == 4:
        new_chord_progression.append('vi')
    if i == 5:
        new_chord_progression.append('vii')

    x = 1

    # While the last chord is not 'i'
    while new_chord_progression[x] != 'i':
        # If chord at position x is 'iii'
        if new_chord_progression[x] == 'iii':
            # Add chord 'vi' as the next chord
            new_chord_progression.append('vi')
            x += 1
        # If chord at position x is 'vi'
        if new_chord_progression[x] == 'vi':
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
        if new_chord_progression[x] == 'ii' or new_chord_progression[x] == 'iv':
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'v' as the next chord
                new_chord_progression.append('v')
                x += 1
            else:
                # Add chord 'ii' as the next chord
                new_chord_progression.append('vii')
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
        if new_chord_progression[x] == 'v':
            # Add chord 'i' as the next chord
            new_chord_progression.append('i')
            x += 1
        # If chord at position x is 'vii'
        if new_chord_progression[x] == 'vii':
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
    print(new_chord_progression)
    return new_chord_progression


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
        if x == 'ii':
            # Create new chord and assign D minor triad notes
            d_min_chord = music21.chord.Chord(["D3", "F3", "A3"])
            # Set chord duration to semibreve/whole
            d_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(d_min_chord)
        # If chord = 'iii'
        if x == 'iii':
            # Create new chord and assign E minor triad notes
            e_min_chord = music21.chord.Chord(["E3", "G3", "B3"])
            # Set chord duration to semibreve/whole
            e_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(e_min_chord)
        # If chord = 'iv'
        if x == 'iv':
            # Create new chord and assign F major triad notes
            f_maj_chord = music21.chord.Chord(["F2", "A2", "C3"])
            # Set chord duration to semibreve/whole
            f_maj_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(f_maj_chord)
        # If chord = 'v'
        if x == 'v':
            # Create new chord and assign G major triad notes
            g_maj_chord = music21.chord.Chord(["G2", "B2", "D3"])
            # Set chord duration to semibreve/whole
            g_maj_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(g_maj_chord)
        # If chord = 'vi'
        if x == 'vi':
            # Create new chord and assign A minor triad notes
            a_min_chord = music21.chord.Chord(["A2", "C3", "E3"])
            # Set chord duration to semibreve/whole
            a_min_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(a_min_chord)
        # If chord = 'vii'
        if x == 'vii':
            # Create new chord and assign B diminished triad notes
            b_dim_chord = music21.chord.Chord(["B2", "D3", "F3"])
            # Set chord duration to semibreve/whole
            b_dim_chord.duration.type = "whole"
            # Add chord to stream
            chord_prog_stream.append(b_dim_chord)
    return chord_prog_stream
