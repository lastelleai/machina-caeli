---
license: apache-2.0
tags:
  - open-source-hardware
  - on-device-ai
  - speech-to-speech
  - robotics
  - 3d-printing
---

# Machina Caeli

**Lastelle AI · OSS-01 · open-source hardware**

*Caelum suspice, stellis ducibus.*

A print-at-home heliocentric mechanism with on-device AI. Eight planets ride concentric rings around a central Sun. One small motor drives a single input shaft, and a gear train turns every planet at its true orbital pace. The machine listens, sees and speaks, all locally, and turns its gears to show the sky for any date you ask about. There is no screen. The gears and pointers are the only output.

Inspired by the Antikythera mechanism. Our own design.

> **Status: concept.** Software for the sky positions and gear search is in place. CAD, print files, schematic and the voice pipeline are in progress.

## Two ways to get it

- **Build it:** every file, the schematic and the parts list are here. Print it and source the parts yourself.
- **Buy the kit:** Lastelle AI sells Machina Caeli packaged and ready to use out of the box.

## What's here

| Path | Contents |
|---|---|
| `hardware/BOM.md` | Parts list for both builds (draft) |
| `hardware/cad/` | STEP files *(coming)* |
| `hardware/print/` | 3MF / STL print files *(coming)* |
| `hardware/schematic/` | KiCad 9 schematics: I/O board, hall board, system wiring for Build A and Build B |
| `docs/gear-train.md` | Tooth counts and per-planet error |
| `software/` | Sky positions, gear search, and later the voice, vision and motor code |

## Two builds

- **Build A, Jetson-class:** NVIDIA Jetson Orin Nano Super Developer Kit.
- **Build B, cheapest reproducible:** Raspberry Pi 5 (8 GB) with the Raspberry Pi AI HAT+ 2.

Benchmarks for both will be published here.

## Accuracy

Each planet's pace comes from JPL's published mean-longitude rates and is matched by its gear ratio. Ring spacing is set by the layout, not real distance. Only pace is to scale. Per-planet error is listed in `docs/gear-train.md`.

## Try the software

```bash
cd software
pip install -e .
python -m machina_caeli.gears        # gear trains and error table
python -m pytest
```

## Licence

Apache License 2.0, covering hardware, software and documentation. See `LICENSE`.

Third-party models used by the builds keep their own licences, listed in `hardware/BOM.md`.

---

Lastelle AI
