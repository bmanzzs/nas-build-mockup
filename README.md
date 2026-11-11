# NAS build mockup

An interactive 3D mockup of my NAS build: a DARKROCK Classico Storage Master case with an ASUS ROG Strix Z390-F, an i9-9900K under a be quiet! Pure Loop 2 360, an EVGA 850 G5, and a passive Tesla V100 PCIe card fed by a 3D-printed intake tunnel. A second V100 can follow later.

**Live page:** https://bmanzzs.github.io/nas-build-mockup/

## What it shows

- The case as it stands: the AIO flipped with its tubes at the rear, one drive cage left in bay 4, and bays 1–3 open.
- One V100 in PCIEX16_1 (now), or a second one in PCIEX16_2 (later).
- One straight tunnel lined up with the card in PCIEX16_1, with the middle and bottom stock front fans removed:
  - a Lian Li 120 on the inside of the steel, screwed to the straightener;
  - the printed straightener (v2, the square 120 × 120 × 20 mm box style with nine vanes);
  - an NZXT Aer P 120;
  - funnel B, running straight into a socket on the card end;
  - collar C on the card end.
- The tunnel's center sits about 29 mm below the middle front fan holes, so fan 1 breathes through parts of the middle and bottom holes. A front adapter on the case's own screw holes is still to design.
- The tunnel only feeds card 1. The two-card view shows that card 2 would still need its own air path.
- The small cards as installed: a FENVI 2.5 GbE card in PCIEX1_1, just above the V100, and the Wi-Fi card in PCIEX16_3.
- An airflow simulation through the whole case, with an X-ray mode that makes the hardware see-through.
- Camera presets (Tunnel, 3/4, Side, Front, Top), dimension lines, full-screen mode (F) and the X-ray toggle (X).

Part sizes come from spec sheets. Positions inside the case are estimates from build photos (roughly ±15 mm) until they're tape-measured. The funnel and collar are drafts until the card arrives and its end is measured.

## Files

- `nas-mockup.html`: the page source, a fragment without `<html>`/`<head>`/`<body>`.
- `index.html`: the full page GitHub Pages serves, generated from the source.
- `build.py`: rebuilds `index.html`. Run `python build.py` after editing `nas-mockup.html`.

Rendering uses [three.js](https://threejs.org/) 0.160.0 loaded from jsDelivr; there's nothing to install.
