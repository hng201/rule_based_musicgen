import music21
import random

quaver = music21.duration.Duration(type='eighth')
crotchet = music21.duration.Duration(type='quarter')
dotted_crochet = music21.duration.Duration(type='quarter', dots=1)
minim = music21.duration.Duration(type='half')
dotted_minim = music21.duration.Duration(type='half', dots=1)
semibreve = music21.duration.Duration(type='whole')
duration_type = [quaver, crotchet, dotted_crochet, minim, dotted_minim, semibreve]
duration_length = [0.5, 1, 1.5, 2, 3, 4]


def generate_note_duration(chord_progression):
    bars = len(chord_progression)
    note_duration = []
    for x in range(bars):
        duration_left = 4
        num = random.randint(0, 5)
        note_duration.append(duration_type[num])
        duration_left = duration_left - duration_length[num]
        while duration_left != 0:
            num = random.randint(0, 5)
            if duration_left >= duration_length[num]:
                note_duration = duration_type[num]
    return note_duration
