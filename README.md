ESP32 Keyboard Matrix Mapper
============================

Description:
------------
This tool is designed to help reverse-engineer raw keyboard matrices—especially useful for retrocomputing or cyberdeck projects where the original keyboard controller is no longer used. It runs on an ESP32-WROOM-32 (30-pin) board and scans a user-defined matrix by driving row lines high and reading column lines for keypresses. It outputs row/column coordinates over serial and prompts the user to label each key for eventual QMK firmware mapping.

Requirements:
-------------
- ESP32-WROOM-32 (30-pin version recommended)
- Keyboard matrix with direct row/column access (not serial-encoded)
- USB cable for flashing and serial communication
- Serial terminal (e.g., PuTTY, Arduino Serial Monitor)

Pin Usage:
----------
The default configuration assumes:
- 5 row lines connected to GPIOs: 13, 12, 14, 27, 26
- 15 column lines connected to GPIOs: 25, 33, 32, 4, 16, 17, 5, 18, 19, 21, 22, 23, 15, 2, 0

You may adjust `NUM_ROWS`, `NUM_COLS`, and the `row_pins[]` / `col_pins[]` arrays in the code to match your hardware setup.

How to Use:
-----------
1. Wire your keyboard matrix to the ESP32 using jumper wires or an FFC breakout (ensure one pin per row and column).
2. Flash the script to the ESP32 using Arduino IDE or PlatformIO.
3. Open a serial terminal at 115200 baud. (Ensure "Both NL & CR" is enabled if using Arduino Serial Monitor.)
4. Press each key as prompted. The tool will:
   - Scan all row/column pairs
   - Detect closed circuits when a key is pressed
   - Prompt you to enter a label (e.g. ESC, A, F1, ENTER)
5. Keymap data will be printed to the serial monitor for you to copy or export.

Output Format:
--------------
Each detected keypress will be printed as:

    Key Press Detected at ROW X / COL Y
    Label this key (e.g. ESC, A, F1): [user input]
    Mapped ROW X COL Y to: [label]

You can use this output to build a keymap array for QMK or other firmware.

Notes:
------
- This script assumes that only one key is pressed at a time. It does not support rollover or ghosting detection.
- Keys may need to be pressed firmly if the matrix uses diodes or passive pull-ups.
- Not compatible with keyboards that use onboard scan code controllers (e.g. those that output serial or PS/2 data).

License:
--------
MIT License — use and modify freely.
