import random

# Array to store generated chord progression
new_chord_progression = []


def generate_chord_progression(key, minNoBar):
    if key <= 3:
        generate_major_chord_progression(minNoBar)
    else:
        generate_minor_chord_progression(minNoBar)
    return new_chord_progression


# Method to generate new chord progression
def generate_major_chord_progression(min_no_bar):
    # Add starting chord for chord progression
    # Number represents chord number
    new_chord_progression.append(1)
    # Generate a random number to determine next chord
    i = random.randint(0, 5)
    if i == 0:
        # Add chord 'ii'
        new_chord_progression.append(2)
    elif i == 1:
        # Add chord 'iii'
        new_chord_progression.append(3)
    elif i == 2:
        # Add chord 'iv'
        new_chord_progression.append(4)
    elif i == 3:
        # Add chord 'v'
        new_chord_progression.append(5)
    elif i == 4:
        # Add chord 'vi'
        new_chord_progression.append(6)
    elif i == 5:
        # Add chord 'vii dim'
        new_chord_progression.append(7)

    x = 1

    # While the last chord is not 'i' or chord progression length is less than minNoBar
    while new_chord_progression[x] != 1 or len(new_chord_progression) < min_no_bar:
        # If chord at position x is 'iii'
        if new_chord_progression[x] == 3:
            # Add chord 'vi' as the next chord
            new_chord_progression.append(6)
            x += 1
        # If chord at position x is 'vi'
        elif new_chord_progression[x] == 6:
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'ii' as the next chord
                new_chord_progression.append(2)
                x += 1
            else:
                # Add chord 'iv' as the next chord
                new_chord_progression.append(4)
                x += 1
        # If chord at position x is 'ii' or 'iv'
        elif new_chord_progression[x] == 2 or new_chord_progression[x] == 4:
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'v' as the next chord
                new_chord_progression.append(5)
                x += 1
            else:
                # Add chord 'vii_dim' as the next chord
                new_chord_progression.append(7)
                x += 1
                # Generate random number to determine next chord
                num = random.randint(0, 1)
                if num == 0:
                    # Add chord 'i' as the next chord
                    new_chord_progression.append(1)
                    x += 1
                else:
                    # Add chord 'iii' as the next chord
                    new_chord_progression.append(3)
                    x += 1
        # If chord at position x is 'v'
        elif new_chord_progression[x] == 5:
            # Add chord 'i' as the next chord
            new_chord_progression.append(1)
            x += 1
        # If chord at position x is 'vii_dim'
        elif new_chord_progression[x] == 7:
            # Generate random number to determine next chord
            num = random.randint(0, 1)
            if num == 0:
                # Add chord 'i' as the next chord
                new_chord_progression.append(1)
                x += 1
            else:
                # Add chord 'iii' as the next chord
                new_chord_progression.append(3)
                x += 1
        else:
            # Select a random chord
            select_random_chord()
            x += 1
    # Display the generated chord progression
    print("major: ", new_chord_progression)


def generate_minor_chord_progression(minNoBar):
    # Add starting chord for chord progression
    new_chord_progression.append(1)
    select_random_chord()

    x = 1
    # While last chord is not 'i' or chord progression length is less than minNoBar
    while new_chord_progression[x] != 1 or len(new_chord_progression) < minNoBar:
        # Generate random number between 0 and 1
        num = random.randint(0, 1)
        # If chord is 'vii'
        if new_chord_progression[x] == 7:
            # Add chord 'iii'
            new_chord_progression.append(3)
            x += 1
        # If chord is 'iii'
        elif new_chord_progression[x] == 3:
            # Add chord 'vi
            new_chord_progression.append(6)
            x += 1
        # If chord is 'vi'
        elif new_chord_progression[x] == 6:
            if num == 0:
                # Add chord 'ii_dim'
                new_chord_progression.append(2)
                x += 1
            else:
                # Add chord 'iv'
                new_chord_progression.append(4)
                x += 1
        # If chord is 'ii_dim'
        elif new_chord_progression[x] == 2:
            if num == 0:
                # Add chord 'v'
                new_chord_progression.append(5)
                x += 1
            else:
                # Add chord 'vii_dim'
                new_chord_progression.append(8)
                x += 1
        # If chord is 'iv'
        elif new_chord_progression[x] == 4:
            num = random.randint(0, 2)
            if num == 0:
                # Add chord 'v'
                new_chord_progression.append(5)
                x += 1
            if num == 1:
                # Add chord 'vii_dim'
                new_chord_progression.append(8)
                x += 1
            else:
                # Add chord 'vii'
                new_chord_progression.append(7)
                x += 1
        # If chord is 'v' or 'vii_dim'
        elif new_chord_progression[x] == 5 or new_chord_progression[x] == 8:
            # Add chord 'i'
            new_chord_progression.append(1)
            x += 1
        else:
            # Select a random chord
            select_random_chord()
            x += 1

    print("Minor: ", new_chord_progression)


def select_random_chord():
    # Generate a random number to determine next chord
    i = random.randint(0, 6)

    if i == 0:
        # Add chord 'ii_dim'
        new_chord_progression.append(2)
    elif i == 1:
        # Add chord 'iii'
        new_chord_progression.append(3)
    elif i == 2:
        # Add chord 'iv'
        new_chord_progression.append(4)
    elif i == 3:
        # Add chord 'v'
        new_chord_progression.append(5)
    elif i == 4:
        # Add chord 'vi'
        new_chord_progression.append(6)
    elif i == 5:
        # Add chord 'vii'
        new_chord_progression.append(7)
    else:
        # Add chord 'vii_dim'
        new_chord_progression.append(8)