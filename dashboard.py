# Code shamelessly copied from Diego Penilla, "Learn Guitar with Python"
# with a few modifications.
# https://betterprogramming.pub/how-to-learn-guitar-with-python-978a1896a47


# standard_tuning EADGBE
six_strings = ['E','A','D','G','B','E']
unique_strings = ['E','A','D','G','B']  

# open G tuning DGDGBD
#six_strings = ['D','G','D','G','B','D']
#unique_strings = ['D','G','B']

# open D tuning DADF#AD
#six_strings = ['D','A','D','F#','A','D'] 
#unique_strings = ['D','F#','A']

#chromatic_notes = ['C','C#','D','D#','E','F',
#                'F#','G','G#','A','A#','B']*3
chromatic_notes = ['C','Db','D','Eb','E','F',
                   'Gb','G','Ab','A','Bb','B']*3


scales = { 
    "major" :            [0, 2, 4, 5, 7, 9, 11],
    "mixolydian":        [0, 2, 4, 5, 7, 9, 10],
    "lydian" :           [0, 2, 4, 6, 7, 9, 11],
    "dorian" :           [0, 2, 3, 5, 7, 9, 10],
    "phrygian" :         [0, 1, 3, 5, 7, 8, 10],
    "minor" :            [0, 2, 3, 5, 7, 8, 10],
    "harmonic_minor" :   [0, 2, 3, 5, 7, 8, 11],
    "melodic_minor" :    [0, 2, 3, 5, 7, 9, 11],
    "blues" :            [0, 3, 5, 6, 7, 10],
    "locrian" :          [0, 1, 3, 5, 6, 8, 10],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonics" :        [0, 3, 4, 5, 7, 9],
    "augmented" :        [0, 3, 4, 7, 8, 11],
    "half_diminished" :  [0, 2, 3, 5, 6, 8, 10],    
}


# initializing a dictionary with the name of strings as dict_keys
strings = {i:0 for i in unique_strings}

for i in strings.keys():

    # finding the index of first note in the string
    start = chromatic_notes.index(i)

    # taking a slice of 21 elements
    strings[i] = chromatic_notes[start:start+21]


def get_notes(key, intervals):

    # finding start of slice
    root = chromatic_notes.index(key)

    # taking 12 consecutive elements
    octave = chromatic_notes[root:root+12]

    # accessing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]


# find the fret positions on each string for the notes in the scale
def find_notes(scale):

    notes_strings = {i:0 for i in unique_strings} 
    
    # for every string 
    for key in strings.keys():
        
        # we create an empty list of indexes
        indexes = []
        
        for note in scale:
            
            # append index where note of the scale is found in
            ind = strings[key].index(note)
            indexes.append(ind)
            
            # because there are 20 frets, there are duplicate notes in the string
            if ind <= 7:
                
                # we must also append these to indexes
                indexes.append(ind+12)
                
        notes_strings[key] = indexes
        
    return notes_strings


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def plot(key, intervals):
 
    fig, ax = plt.subplots( figsize=(20,6) )
    
    # Plot Strings
    for i in range(1,7):
        ax.plot([i for a in range(22)] )

    # Plotting Frets
    for i in range(1,21):
        
        # decorates the twelve fret with a gray and thick fret
        if i == 12:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        
        # trace a vertical line (a fret)
        ax.axvline(x=i, color='black', linewidth=0.5)

        ax.set_axisbelow(True)


    # setting height and width of displayed guitar
    ax.set_xlim([0.5, 21])
    ax.set_ylim([0.5, 6.5])


    # finding note positions of the scale in the guitar
    scale = get_notes(key, intervals)
    to_plot = find_notes(scale)

    print ( strings )
    print()
    print (scale )
    print()
    print ( to_plot )
 
    # for every note of the scale in every string make a circle
    # with the note's name as label in the corresponding fret
    for y_val, key in zip([1,2,3,4,5,6], six_strings):
        
        for i in to_plot[key]:

            x = i+0.5  # shift the circles to the right
            p = mpatches.Circle((x, y_val), 0.2, color='blue')
            ax.add_patch(p)

            note = strings[key][i]
            # if note is the root make it a bit bigger
            if note == scale[0]:
                font=14.
                note_color = 'red'
            else:
                font=12
                note_color = 'white'
            
            # add label to middle of the circle
            ax.annotate(note, (i+0.5, y_val), color=note_color, weight='bold', 
                            fontsize=font, ha='center', va='center')


    plt.title('_| _| _| _| _|'*16)

    plt.yticks(np.arange(1,7), six_strings)
    
    plt.xticks(np.arange(21)+0.5, np.arange(0,21))

    plt.show()

plot('E', scales['minor_pentatonic'])
