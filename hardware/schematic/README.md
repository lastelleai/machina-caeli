# Schematics (KiCad 9)

Checked and exported to PDF automatically by GitHub Actions (`.github/workflows/schematics.yml`) using the official `kicad/kicad:9.0` image. The PDFs are attached to each run.

| Project | Contents |
|---|---|
| `machina-io` | I/O board MC-IO-01: 12 V entry, TMC2209 driver, header buffer, motor and hall connectors |
| `machina-hall` | Hall board MC-HALL-01: DRV5032 homing switch |
| `machina-system-a` | Build A wiring: Jetson Orin Nano Super, I/O board, ReSpeaker, camera, motor, hall, cables |
| `machina-system-b` | Build B wiring: Raspberry Pi 5 + AI HAT+ 2, same peripherals |
| `lib/machina.kicad_sym` | Symbol library used by all four |
