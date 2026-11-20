# Bill of materials (draft)

## Shared by both builds

| Part | Pick | Notes |
|---|---|---|
| Mic array + speaker amp | Seeed ReSpeaker XVF3800 USB 4-Mic Array (non-XIAO version) | Flash the 48 kHz / 2-channel USB firmware. USB Audio Class 2.0. |
| Speaker | 4 Ω, 5 W full-range driver, mono | Driven by the board's LM48511 amplifier (minimum load 4 Ω). |
| Camera | Raspberry Pi Camera Module 2 (Sony IMX219) | 15-to-22-pin CSI cable for the Jetson. |
| Bearings | 608 | Press-fit. |
| Motor | ADI Trinamic QSH4218-41-10-035 | NEMA 17, 1.0 A, 35 Ncm, 4-wire. |
| Driver | Watterott SilentStepStick TMC2209 v2.0 | Plugs into the I/O board. |
| Homing magnet | Diametric or axial magnet on the Earth ring | Read by the hall board. |
| Power | Mean Well GST90A12-P1M | 12 V, 6.67 A, 2.5 x 5.5 mm plug. Feeds the I/O board. |

## Build A: Jetson-class

| Part | Pick |
|---|---|
| Compute | NVIDIA Jetson Orin Nano Super Developer Kit (8 GB) |
| OS | JetPack 6.2 |
| Power | Taken from the I/O board (J2, 12 V) |

Models: Silero VAD · Parakeet TDT 0.6B v3 (speech-to-text) · Qwen3.5-4B, 4-bit, via llama.cpp (conversation and vision) · Kokoro-82M (voice).

## Build B: cheapest reproducible

| Part | Pick |
|---|---|
| Compute | Raspberry Pi 5, 8 GB |
| Accelerator | Raspberry Pi AI HAT+ 2 (Hailo-10H, 8 GB onboard) |
| Power | Raspberry Pi 27W USB-C Power Supply (Pi only; motor stays on the 12 V supply) |

Models: Silero VAD (CPU, ONNX Runtime) · Whisper-Small on the HAT (speech-to-text) · Qwen3-VL-2B-Instruct on the HAT (conversation and vision) · Kokoro-82M on the CPU (voice).

## Model licences

Silero VAD MIT · Parakeet TDT 0.6B v3 CC BY 4.0 (NVIDIA) · Qwen3.5-4B Apache-2.0 · Qwen3-VL-2B-Instruct Apache-2.0 · Kokoro-82M Apache-2.0 · Whisper MIT.

## Print

Filament, printer settings and per-part print times will be listed with the print files.

## I/O board MC-IO-01 (`schematic/machina-io`)

| Ref | Qty | Part | Manufacturer part number |
|---|---|---|---|
| J1, J2 | 2 (J2 Build A only) | DC jack 2.5 x 5.5 mm, 8 A | Same Sky PJ-063AH |
| J5 | 1 | JST XH 4-way vertical | JST B4B-XH-A(LF)(SN) |
| J6 | 1 | 2x20 2.54 mm box header | Amphenol T821140A1S100CEU |
| J7 | 1 | JST XH 3-way vertical | JST B3B-XH-A(LF)(SN) |
| U1 | 1 | Stepper driver module | Watterott SilentStepStick TMC2209 v2.0 |
| U1 socket | 2 | 1x8 2.54 mm socket strip | Samtec SSW-108-01-T-S |
| U2 | 1 | Quad buffer, SOIC-14 | Texas Instruments SN74LVC125ADR |
| C1 | 1 | 100 µF 35 V low-ESR, 8 mm, 3.5 mm pitch | Panasonic EEU-FR1V101 |
| C2, C3 | 2 | 100 nF 50 V X7R 0603 | Murata GRM188R71H104KA93D |
| D1 | 1 | Schottky, SOT-23 | Nexperia BAT54,215 |
| R1, R2, R3 | 3 | 100 kΩ 1 % 0603 | Yageo RC0603FR-07100KL |
| R4 | 1 | 330 Ω 1 % 0603 | Yageo RC0603FR-07330RL |

## Hall board MC-HALL-01 (`schematic/machina-hall`)

| Ref | Qty | Part | Manufacturer part number |
|---|---|---|---|
| U1 | 1 | Hall switch, omnipolar, push-pull, SOT-23 | Texas Instruments DRV5032FADBZR |
| C1 | 1 | 100 nF 50 V X7R 0603 | Murata GRM188R71H104KA93D |
| J1 | 1 | JST XH 3-way vertical | JST B3B-XH-A(LF)(SN) |

## Cables

| Cable | From | To | Specification |
|---|---|---|---|
| W1 (Build A) | I/O J2 | Jetson J16 | 5.5 x 2.5 mm plug both ends, centre +, 18 AWG, 150 mm |
| W2 | I/O J6 | SBC 40-pin | 40-way 1.27 mm ribbon, 2x20 IDC sockets both ends, 1:1, 150 mm |
| W3 | SBC USB-A | ReSpeaker USB-C | USB-A to USB-C, 300 mm |
| W4 | ReSpeaker speaker JST | Speaker | 2-way speaker lead |
| W5 | SBC camera port | Camera Module 2 | Raspberry Pi camera cable, 22-pin to 15-pin, 200 mm |
| W6 | I/O J5 | Motor | Motor leads in JST XHP-4 with SXH-001T-P0.6 contacts |
| W7 | I/O J7 | Hall J1 | JST XHP-3 both ends, 1:1, 26 AWG, 300 mm |
| W8 (Build B) | Pi 5 PCIe | AI HAT+ 2 | Supplied with the HAT |
