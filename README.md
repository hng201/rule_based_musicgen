# rule_based_musicgen
A rule based system which generates homophonic music using a set of generators within the system. Musical aspects of the system have been implemented using the external library `music21`. \
\
Link to music21:\
https://github.com/cuthbertLab/music21 \
\
The system restricts outputs to a time signature of 4/4 and limits the number of major and minor keys that can be selected for generating homophonic music.
Accompaniments are also restricted to 3 octaves and the melody is restricted to one octave. 
Modification of certain musical aspects of the output is possible by modifying the music parameters stored within the file `musicparam.py`
## Modifying Music Parameters
The music parameters are assigned numbers to represent the option selected or requirements depending on the parameter. \
These parameters are located within the file `musicparam.py` and can be modifed as shown below:
* `key`: The major or minor key of the music composition.
  * Major keys:
    * C major = 0
    * G major = 1
    * D major = 2
    * A major = 3
  * Minor Keys: 
    * A minor = 4
    * E minor = 5
    * B minor = 6
    * F# minor = 7
* `min_no_bar`: The minimum number of bars for the outputted music composition.
  * The generated composition may have more bars than this.
* `accomp_rest_limit`: The total duration of rests that can exist in one bar for the accompaniment.
  * Maximum limit is 4.
* `melody_rest_limit`: The total duration of rests that can exist in one bar for the melody.
  * Maximum limit is 4.
* `accomp_type`: The accompniment style to generate for the music compostion.
  * Accompaniment styles available:
    * Chord-based = 0
    * Arpeggio-based = 1
    * Chord and Arpeggio = 2
