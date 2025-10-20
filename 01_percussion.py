# Instrument: PERCUSSION (soft/brush kit)
moveTo(0)

from random import random

KICK, SNARE, HAT = 0, 2, 4

BARS = 16
SWING = 0.024   # small feel shift on off-eighths

# base levels
HAT_V   = 40
KICK_V  = 60
SNARE_V = 46

def v(x):
    x = int(x)
    return 0 if x < 0 else (127 if x > 127 else x)

for bar in range(BARS):
    # two-phrase arc inside each 4-bar group
    soft_phrase = (bar % 4 in (0, 3))
    ghost_prob  = 0.12 if soft_phrase else 0.18
    hat_bias    = -2 if soft_phrase else +3

    for i in range(8):  # 8 eighths per bar
        off = (i % 2) == 1
        dur = (0.5 - SWING) if off else (0.5 + SWING)

        # stack events first (no time advance)
        if i == 0:  # strong downbeat
            playNote(KICK, beats=0, velocity=v(KICK_V + (-4 if soft_phrase else 0)))
        if i == 4 and (bar % 2 == 1):  # light heartbeat on 3 every other bar
            playNote(KICK, beats=0, velocity=v(KICK_V - 10))

        if i in (2, 6):  # back-taps
            playNote(SNARE, beats=0, velocity=v(SNARE_V + (-6 if soft_phrase else 0)))
        if i == 3 and random() < ghost_prob:
            playNote(SNARE, beats=0, velocity=v(SNARE_V - 12))

        # hats advance time (visible grid)
        hat_push = 6 if i in (0, 4) else 0
        playNote(HAT, beats=dur, velocity=v(HAT_V + hat_bias + hat_push))

        # small lift at phrase starts
        if i == 0 and (bar % 4 == 0):
            playNote(SNARE, beats=0, velocity=v(SNARE_V - 8))
