# Instrument: KEYS (harp/pizz/clean)
moveTo(0)

BARS = 16
KEY  = 'A'
OCT  = 3

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,
        'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}
def midi(n='A', o=3): return 12*(o+1) + NOTE[n]
def pent_major(root):  return [root+i for i in (0,2,4,7,9)]
def deg(scale, d):     return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

root  = midi(KEY, OCT)
scale = pent_major(root)

# Different grouping from the other set: 2–3–3 across the bar (still 8 eighths)
groups = (2, 3, 3)
pattern_degs = [1, 5,   2, 3, 5,   6, 1, 5]  # map to 8 slots

pedal_plan = [1, 1, 6, 1]
BAR_DYN    = (-2, +2, +4, 0)

for b in range(BARS):
    dyn = BAR_DYN[b % 4]
    ped = deg(scale, pedal_plan[b % 4])

    seq = []
    # first note of each group anchors to pedal
    anchors = {0, groups[0], groups[0]+groups[1]}
    for idx, d in enumerate(pattern_degs):
        seq.append(ped if idx in anchors else deg(scale, d))

    # light lift on group leaders
    for k, n in enumerate(seq):
        lift = 6 if k in anchors else 0
        playNote(n, beats=0.5, velocity=54 + dyn + lift)
