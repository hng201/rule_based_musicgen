class MusicParam:
    def __init__(self):
        # Major Keys: 0 = C, 1 = G, 2 = D, 3 = A
        # Minor Keys: 4 = A, 5 = E, 6 = B, 7 = F#
        self.key = 5
        # Set minimum no of bars for chord progression generation
        self.min_no_bar = 12
        # Set maximum number of rests that can be present in each bar
        # This refers to rest notes and not note duration
        self.rest_bar_limit = 2
