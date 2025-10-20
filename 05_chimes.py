# Instrument: BELLS (celesta/music box)
moveTo(0)

BARS = 16
KEY  = 'A'
OCT  = 5

NOTE = {'C':0,'Cs':1,'Db':1,'D':2,'Ds':3,'Eb':3,'E':4,'F':5,'Fs':6,'Gb':6,
        'G':7,'Gs':8,'Ab':8,'A':9,'As':10,'Bb':10,'B':11}
def midi(n='A', o=5): return 12*(o+1) + NOTE[n]
def pent_major(root):  return [root+i for i in (0,2,4,7,9)]
def deg(scale, d):     return scale[{1:0,2:1,3:2,5:3,6:4}[d]]

scale = pent_major(midi(KEY, OCT))

for b in range(BARS):
    # start of 4-bar phrase
    if b % 4 == 0:
        playNote(deg(scale,1), beats=0.5, velocity=56)
        playNote(deg(scale,5), beats=0.5, velocity=54)
    # mid-phrase hint
    if b % 4 == 2:
        playNote(deg(scale,3), beats=0.5, velocity=52)
    # phrase end
    if b % 4 == 3:
        playNote(deg(scale,6), beats=0.5, velocity=54)
        playNote(deg(scale,1), beats=1.0, velocity=58)
