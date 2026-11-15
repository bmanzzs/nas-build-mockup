# NAS build mockup

An interactive 3D mockup of my NAS build: a DARKROCK Classico Storage Master case with an ASUS ROG Strix Z390-F, an i9-9900K under a be quiet! Pure Loop 2 360, an EVGA 850 G5, and a passive Tesla V100 PCIe card fed by a 3D-printed intake tunnel.

**Live page:** https://bmanzzs.github.io/nas-build-mockup/

## What it shows

- The case as it stands: the AIO flipped with its tubes at the rear, one drive cage left in bay 4, and bays 1–3 open.
- One V100 in PCIEX16_1.
- Tunnel v6, with the middle and bottom stock front fans removed. The front fans, the fan stack and the card line up in one column across the case. Front to back:
  - adapter v1 (already printed, black PETG), hung inside the front steel on two case screws through the middle fan's top holes; its slots let it slide ±4 mm up or down, and the stack floats 1.5 mm off the steel;
  - an Arctic P12 Pro (fan 1), screwed to the adapter with its four fan screws, so the front uses six screws in all;
  - straightener v4 and a second Arctic P12 Pro (fan 2);
  - rail frame v3 on fan 2's back, with a dovetail rail and a lead-in chamfer at its glass end;
  - four printed snap pins from the rail frame through fan 2 and the straightener, clicking into fan 1's open corners;
  - duct v6, one piece from the rail to the card end. The adapter hangs the stack 27.5 mm below the card's axis, so the duct climbs that much with straight walls. Its sleeve is the 98.5 × 37 mm of a printed test frame that went on snug, shaped to the card end's outline from close-up photos, seals with a soft lip, and is held by the card's three end screws through a plate on its end strip; a trough lets the EPS 8-pin lead leave in a gentle curve.
- The Slide-in toggle shows how it goes together: the duct is screwed to the card at the bench, and its flange slides into the rail as the card goes into its slot.
- The tunnel parts are the real print models: a GLB written by the same Blender script as the STL files, stored base64 in `v100_tunnel_v6.json`.
- The small cards as installed: a FENVI 2.5 GbE card in PCIEX1_1, just above the V100, and the Wi-Fi card in PCIEX16_3.
- An airflow simulation through the whole case, with an X-ray mode that makes the hardware see-through.
- Camera presets (Tunnel, 3/4, Side, Front, Top), dimension lines, full-screen mode (F) and the X-ray toggle (X).

Part sizes come from spec sheets. Positions inside the case come from ruler photos (roughly ±3 mm). The snap pins, the dovetail and the lip are sized from a printed snap test; the card end's size comes from a printed test frame that fit, and its outline and screw holes from a close-up photo scaled to it (about ±0.5 mm).

## Files

- `nas-mockup.html`: the page source, a fragment without `<html>`/`<head>`/`<body>`.
- `index.html`: the full page GitHub Pages serves, generated from the source.
- `build.py`: rebuilds `index.html`. Run `python build.py` after editing `nas-mockup.html`.
- `v100_tunnel_v6.json`: the tunnel's printed parts, loaded by the page.

Rendering uses [three.js](https://threejs.org/) 0.160.0 and its GLTFLoader, loaded from jsDelivr; there's nothing to install.
