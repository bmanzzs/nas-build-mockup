# NAS build mockup

An interactive 3D mockup of my NAS build: a DARKROCK Classico Storage Master case with an ASUS ROG Strix Z390-F, an i9-9900K under a be quiet! Pure Loop 2 360, an EVGA 850 G5, and passive Tesla V100 PCIe cards (one now, a second on its way) fed by a 3D-printed intake tunnel.

**Live page:** https://bmanzzs.github.io/nas-build-mockup/

## What it shows

- The case as it stands: both drive cages in bays 3 and 4, bays 1 and 2 open, and the AIO tubes looping down over the card.
- Two V100s, in PCIEX16_1 and PCIEX16_2 (three slots apart, x8/x8), fed by the twin duct v11. The **Card 2** toggle, on by default, switches to the one-card build with duct v10.
- Tunnel v10, with the middle and bottom stock front fans removed. The front fans, the fan stack and the card line up in one column across the case. Front to back:
  - adapter v1 (already printed, black PETG), hung inside the front steel on two case screws through the middle fan's top holes; its slots let it slide ±4 mm up or down, and the stack floats 1.5 mm off the steel;
  - an Arctic P12 Pro (fan 1), screwed to the adapter with its four fan screws, so the front uses six screws in all;
  - straightener v4 and a second Arctic P12 Pro (fan 2);
  - rail frame v3 on fan 2's back, with a dovetail rail and a lead-in chamfer at its glass end;
  - four printed snap pins from the rail frame through fan 2 and the straightener, clicking into fan 1's open corners;
  - duct v10, one piece from the rail to the card end. The adapter hangs the stack 27.5 mm below the card's axis, so the duct climbs that much with straight walls. Its sleeve has rigid walls fitted to the card end with three printed test pieces (the last one fit perfectly), and is held by the card's three end screws through a plate on its end strip; two fills in front of the end strip steer the air down into the heatsink fins, and a trough lets the EPS 8-pin lead leave in a gentle curve.
- Twin duct v11 (two cards): v10 grown to both card ends, with the same flange, rail and fan stack. One block holds two of the fitted sleeves 60.96 mm apart, each screwed to its card with its own plate and fills, and a web between the cards splits the stack's air between them. Card 2's EPS lead goes up a trough into the web and out through a window in the duct's glass side.
- The Slide-in toggle shows how it goes together: the duct is screwed to the card at the bench, and its flange slides into the rail as the card goes into its slot.
- The tunnel parts are the real print models: GLBs written by the same Blender scripts as the STL files, stored base64 in `v100_tunnel_v10.json` (one card) and `v100_tunnel_v11.json` (two).
- The small cards as installed: a FENVI 2.5 GbE card in PCIEX1_1, just above the V100, and the Wi-Fi card in PCIEX16_3.
- Sag bracket v1 under both cards: a printed jack stand on the PSU shroud, screwed through one long slot into two holes near the shroud's glass edge. A thumb nut on its threaded post (3 mm a turn) lifts a fork whose two arms sit under the cards, 60.96 mm apart. It is the print script's own model, like the tunnel parts.
- An airflow simulation through the whole case, with an X-ray mode that makes the hardware see-through.
- Focus on any part: click or tap it (or its label, or Show in the build checklist) and the camera zooms in on it where it sits. It stays solid with an accent outline while the rest of the PC fades to a faint ghost, and the view turns slowly round it (it pauses while you drag, and picks up again a few seconds after). A small card says what the part is, with its checklist tick as one quiet line (click it to find the row). The arrows (or ← →, or a swipe on the card, or a tap on another part) move the focus; the round ✕, Esc or a tap on empty space pull back out.
- Camera presets (Tunnel, 3/4, Side, Front, Top, Back), dimension lines, full-screen mode (F) and the X-ray toggle (X).
- The switch row folds away to one Switches button (folded at first on phones), and each part in the build checklist has an eye button that hides it in the model or brings it back. A Checkmarks switch turns off the ✓ marks on ticked parts' labels and their green edges.

Part sizes come from spec sheets. Positions inside the case come from ruler photos (roughly ±3 mm). The snap pins and the dovetail are sized from a printed snap test; the sleeve started from a printed test frame and close-up photos, then was fitted on the card with three printed test pieces.

## Files

- `nas-mockup.html`: the page source, a fragment without `<html>`/`<head>`/`<body>`.
- `index.html`: the full page GitHub Pages serves, generated from the source.
- `build.py`: rebuilds `index.html`. Run `python build.py` after editing `nas-mockup.html`.
- `v100_tunnel_v10.json`, `v100_tunnel_v11.json`: the tunnel's printed parts for one card and for two, loaded by the page.
- `v100_sag_bracket_v1.json`: the sag bracket (base and post, nut, fork) in the case's own frame, loaded by the page.

Rendering uses [three.js](https://threejs.org/) 0.160.0 and its GLTFLoader, loaded from jsDelivr; there's nothing to install.
