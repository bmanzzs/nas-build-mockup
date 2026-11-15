# NAS build mockup

An interactive 3D mockup of my NAS build: a DARKROCK Classico Storage Master case with an ASUS ROG Strix Z390-F, an i9-9900K under a be quiet! Pure Loop 2 360, an EVGA 850 G5, and a passive Tesla V100 PCIe card fed by a 3D-printed intake tunnel.

**Live page:** https://bmanzzs.github.io/nas-build-mockup/

## What it shows

- The case as it stands: the AIO flipped with its tubes at the rear, one drive cage left in bay 4, and bays 1–3 open.
- One V100 in PCIEX16_1.
- Tunnel v3, a straight shot on the card's own axis, with the middle and bottom stock front fans removed. Front to back:
  - adapter v2, hung inside the front steel on two case screws; its slotted windows let the stack float into line before the screws are tightened;
  - an Arctic P12 Pro (fan 1), straightener v3 and a second Arctic P12 Pro (fan 2);
  - rail frame v1 on fan 2's back, with a dovetail rail;
  - four printed snap pins through the whole stack instead of screws;
  - duct v3, one piece from the rail to the card end. It slips over the card end, seals with a soft lip, and has a trough so the EPS 8-pin lead leaves in a gentle curve.
- The Slide-in toggle shows how it goes together: the duct goes on the card at the bench, and its flange slides into the rail as the card goes into its slot.
- The tunnel parts are the real print models: a GLB written by the same Blender script as the STL files, stored base64 in `v100_tunnel_v3.json`.
- The small cards as installed: a FENVI 2.5 GbE card in PCIEX1_1, just above the V100, and the Wi-Fi card in PCIEX16_3.
- An airflow simulation through the whole case, with an X-ray mode that makes the hardware see-through.
- Camera presets (Tunnel, 3/4, Side, Front, Top), dimension lines, full-screen mode (F) and the X-ray toggle (X).

Part sizes come from spec sheets. Positions inside the case come from ruler photos (roughly ±3 mm). The snap fits and the lip get tuned from a printed snap test.

## Files

- `nas-mockup.html`: the page source, a fragment without `<html>`/`<head>`/`<body>`.
- `index.html`: the full page GitHub Pages serves, generated from the source.
- `build.py`: rebuilds `index.html`. Run `python build.py` after editing `nas-mockup.html`.
- `v100_tunnel_v3.json`: the tunnel's printed parts, loaded by the page.

Rendering uses [three.js](https://threejs.org/) 0.160.0 and its GLTFLoader, loaded from jsDelivr; there's nothing to install.
