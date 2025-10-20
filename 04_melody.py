# Instrument: LEAD (flute/soft lead)
moveTo(0)

import random
BARS, KEY, OCT = 16, 'A', 4
DENSITY = 0.55
SEED    = 13
random.seed(SEED)

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,
        'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}
def midi(n='A', o=4): return 12*(o+1) + NOTE[n]
def pent_major(root):  return [root+i for i in (0,2,4,7,9)]
def deg(scale, d):     return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

scale = pent_major(midi(KEY, OCT))

NEIGH = {1:[1,2,3,5], 2:[1,2,3,5], 3:[2,3,5,6], 5:[1,2,3,5,6], 6:[3,5,6,1]}
prev  = 1

def choose_next(p):
    return random.choice(NEIGH.get(p, [1,2,3,5,6]))

def grace_for(target):
    if target in (1,2): return 6
    if target in (5,6): return 3
    return 2

for bar in range(BARS):
    for step in range(8):  # 8 eighths per bar
        strong = step in (0, 4)
        if strong or random.random() < DENSITY:
            d = choose_next(prev)
            if strong and random.random() < 0.7:
                g = grace_for(d)
                playNote(deg(scale, g), beats=0.25, velocity=60)
                playNote(deg(scale, d), beats=0.75, velocity=66)
            else:
                length = 1.0 if random.random() < 0.30 else 0.5
                playNote(deg(scale, d), beats=length, velocity=64)
            prev = d
        else:
            rest(0.5)
    # bar-end ease
    cad = 1 if (bar % 4 in (1,3)) else 5
    playNote(deg(scale, cad), beats=0.25, velocity=62)
    rest(0.25)
