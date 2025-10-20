# Instrument: BASS (acoustic/soft electric)
moveTo(0)

BARS = 16
KEY  = 'A'
OCT  = 2

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,
        'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}

def midi(n='A', o=2): return 12*(o+1) + NOTE[n]
def pent_major(root):  return [root+i for i in (0,2,4,7,9)]  # 1,2,3,5,6
def deg(scale, d):     return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

root  = midi(KEY, OCT)
scale = pent_major(root)

plan_degs = [1, 1, 6, 1]  # 4-bar frame
BAR_DYN   = (-3, +1, +3, -1)

for b in range(BARS):
    dyn  = BAR_DYN[b % 4]
    rdeg = plan_degs[b % 4]
    base = deg(scale, rdeg)

    # 1 beat center
    playNote(base,           beats=1.0, velocity=64 + dyn)
    # 1 beat gentle rise
    playNote(deg(scale, 2),  beats=0.5, velocity=58 + dyn)
    playNote(deg(scale, 3),  beats=0.5, velocity=60 + dyn)
    # 1 beat fifth
    playNote(deg(scale, 5),  beats=1.0, velocity=62 + dyn)
    # 1 beat turn back
    playNote(deg(scale, 6),  beats=0.5, velocity=58 + dyn)
    playNote(base,           beats=0.5, velocity=64 + dyn)
