import random

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
            num = random.randint(0,1)
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








