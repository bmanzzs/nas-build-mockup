# NAS build mockup

An interactive 3D mockup of my NAS build: a DARKROCK Classico Storage Master case with an ASUS ROG Strix Z390-F, an i9-9900K under a be quiet! Pure Loop 2 360, an EVGA 850 G5, and one or two passive Tesla V100 PCIe cards fed by a 3D-printed PETG intake duct.

**Live page:** https://bmanzzs.github.io/nas-build-mockup/

## What it shows

- Three layouts: the drive cages as built today (bays 1–2), the plan (bays 3–4), and a fallback (bays 2–3).
- One V100 in either x16 slot, or two cards in both slots with a dual duct.
- The duct: two front intake fans feed two Arctic P12 Max fans in series, spaced 20 mm apart with a printed straightener between them, then a funnel down to the card end.
- How it mounts: a small collar screws to the card end on the bench, and the duct body drops in from the open side and locks on with thumbscrews. The Collar and Fan stack views zoom in on every screw, and Exploded pulls the body out the way it goes in.
- An airflow simulation through the whole case, with an X-ray mode that makes the hardware see-through.
- Full-screen mode (F), X-ray toggle (X), exploded view (E), and dimension lines.

Part sizes come from spec sheets. Positions inside the case are estimates from build photos (roughly ±15 mm) until they're tape-measured.

## Files

- `nas-mockup.html`: the page source, a fragment without `<html>`/`<head>`/`<body>`.
- `index.html`: the full page GitHub Pages serves, generated from the source.
- `build.py`: rebuilds `index.html`. Run `python build.py` after editing `nas-mockup.html`.

Rendering uses [three.js](https://threejs.org/) 0.160.0 loaded from jsDelivr; there's nothing to install.
