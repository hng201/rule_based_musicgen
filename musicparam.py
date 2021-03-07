class MusicParam:
    def __init__(self):
        # Major Keys: 0 = C, 1 = G, 2 = D, 3 = A
        # Minor Keys: 4 = A, 5 = E, 6 = B, 7 = F#
        self.key = 5
        # Set minimum no of bars for chord progression generation
        self.min_no_bar = 12
        # Set rest limit per bar
        # This refers to total duration of rest notes
        # Max is 4 due to each bar being 4 beats
        # Set rest limit for accompaniment
        self.accomp_rest_limit = 1.5
        # Set rest limit for melody
        self.melody_rest_limit = 1
        # Set accompaniment type
        # 0 = chord based, 1 = arpeggio based, 2 = chord and arpeggio
        self.accomp_type = 1
