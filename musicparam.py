class MusicParam:
    def __init__(self):
        # Major Keys: 0 = C, 1 = G, 2 = D, 3 = A
        # Minor Keys: 4 = A, 5 = E, 6 = B, 7 = F#
        self.key = 7
        # Set minimum no of bars for chord progression generation
        self.min_no_bar = 12
        # Set total duration for rests in the composition
        # This refers to maximum duration of all rests counted
        # within the composition
        # Set rest limit for accompaniment
        self.accomp_rest_limit = 13.25
        # Set rest limit for melody
        self.melody_rest_limit = 6.75
