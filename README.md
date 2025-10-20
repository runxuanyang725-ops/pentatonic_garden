# Pentatonic Garden (TunePad)

A compact music sketch in TunePad using a five-note major pentatonic palette. Each script is meant for a separate Code cell in the order shown below. The arrangement aims for a calm, unforced texture with light movement and clear phrasing.

## Layout
- `cells/01_percussion.py` – brushy kit, hats carry time, gentle ghosts.
- `cells/02_bassline.py` – slow step motion around the center.
- `cells/03_picking.py` – plucked pattern with pedal anchors.
- `cells/04_melody.py` – singable line with occasional graces.
- `cells/05_chimes.py` – sparse markers at phrase edges.

## How to use (TunePad)
1. Create a new project and add **five** Code cells.
2. Set instruments to match the file names (soft kit, bass, keys/harp, lead, bells).
3. Paste each file’s code into the corresponding cell, top to bottom.
4. Run each cell, then play. Use Mute/Solo to check balance.

## Parameters you’ll want to try
- Global key and register per file: `KEY`, `OCT`.
- Percussion feel: `SWING`, ghost probability, base velocities.
- Picking shape: group boundaries and the pedal plan.
- Melody density and random seed for variation.

## Notes on reliability
- One integer velocity per event.
- Let one event per step advance time; stack others at the same timestamp with `beats=0`.
- Keep textures light; short monophonic lines help browser timing.

## License
See `LICENSE`.

