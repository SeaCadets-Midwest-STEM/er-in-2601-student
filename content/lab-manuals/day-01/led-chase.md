---
title: "Lab: LED Chase Pattern â€” Loops That Do the Work"
description: "Make three LEDs chase each other using a for loop."
date: 2026-07-26
publishDate: 2026-07-26
session: "1C"
---

> **Session:** Session 1C â€” LED Chase Pattern: Loops That Do the Work
> **Audience:** All teams (student-facing)
> **Time Allotted:** 40 minutes
> **Team Size:** 3 students per station
> **Prerequisites:** Session 1B (Hello Matrix) completed â€” LED on Pin 9 already wired
>
> Make three LEDs "chase" each other using a `for` loop â€” and discover how one line of code can control multiple pins.

---

## SAFETY

> **SAFETY:** 5V logic. No high voltage. No heat. Standard electronics safety: do not short 5V to GND with a wire while the board is powered.

---

## Objective

Make three LEDs chase each other using a `for` loop â€” and discover how one line of code can control multiple pins.

---

## Parts List

Verify all items are present at your station. Check each box.

| Part | Qty | Found? |
| :--- | :--- | :--- |
| Arduino Uno Q (mounted at station) | 1 | [ ] |
| Breadboard (830-point, mounted at station) | 1 | [ ] |
| Red LED (5mm) â€” from Lab 1B | 1 | [ ] |
| **Yellow LED (5mm)** | **1** | **[ ] NEW** |
| **Green LED (5mm)** | **1** | **[ ] NEW** |
| 220Î© resistors | 3 | [ ] (1 from Lab 1B, **2 NEW**) |
| Jumper wires (female-female) | 6+ | [ ] |

---

## Procedure

### Step 1 â€” Wire Two More LEDs (15 min)

**Hardware Tech leads. Observer reads steps. Coder watches for next step.**

Add a yellow LED on Pin 8 and a green LED on Pin 7, using the same wiring pattern as the red LED on Pin 9.

#### Wiring pattern

Each LED follows the same pattern:

- **Green LED:** Arduino Pin 7 â†’ jumper â†’ 220Î© resistor â†’ LED long leg (anode) â†’ LED short leg (cathode) â†’ GND
- **Yellow LED:** Arduino Pin 8 â†’ jumper â†’ 220Î© resistor â†’ LED long leg (anode) â†’ LED short leg (cathode) â†’ GND
- **Red LED:** Arduino Pin 9 â†’ (already wired from Lab 1B)

#### Steps

1. **Place the yellow LED** on the breadboard. Long leg (anode) on one row, short leg (cathode) on a different row.
2. **Place a 220Î© resistor** from the yellow LED's long leg row to a free breadboard row.
3. **Connect** a jumper wire from that resistor row to **Arduino Pin 8**.
4. **Connect** the yellow LED's short leg to the **GND rail** with a jumper wire.
5. **Repeat steps 1â€“4** for the green LED, connecting to **Arduino Pin 7**.
6. **Verify:** All three LED short legs connect to GND. Each LED has its own 220Î© resistor. Each resistor connects to a different pin (7, 8, 9).

> **EXPECTED RESULT:** Nothing visible yet (no code controlling Pins 7 and 8). Three LEDs on the breadboard, each with a resistor, each connected to a different pin.

#### Self-check

- [ ] Green LED: Pin 7 â†’ resistor â†’ LED long leg â†’ LED short leg â†’ GND
- [ ] Yellow LED: Pin 8 â†’ resistor â†’ LED long leg â†’ LED short leg â†’ GND
- [ ] Red LED: Pin 9 â†’ resistor â†’ LED long leg â†’ LED short leg â†’ GND (from Lab 1B)
- [ ] No LEDs sharing a resistor (each LED has its own)

**Call an instructor to verify wiring before proceeding.**

---

### Step 2 â€” The Chase Pattern (25 min)

**Coder types. Observer reads instructions. Hardware Tech watches for mistakes.**

#### 2a â€” Create a new sketch

Open Arduino App Lab and create a new sketch.

#### 2b â€” Type the code

```cpp
/*
 * Session 1C: LED Chase Pattern
 * Team ___ â€” Creation Station #___
 * Purpose: Make 3 LEDs chase using a for loop
 * Expected result: Lights travel green to yellow to red, then reverse
 */

void setup() {
  pinMode(7, OUTPUT);  // Green
  pinMode(8, OUTPUT);  // Yellow
  pinMode(9, OUTPUT);  // Red
}

void loop() {
  // Forward chase
  for (int i = 7; i <= 9; i = i + 1) {
    digitalWrite(i, HIGH);
    delay(150);
    digitalWrite(i, LOW);
  }

  // Backward chase
  for (int i = 9; i >= 7; i = i - 1) {
    digitalWrite(i, HIGH);
    delay(150);
    digitalWrite(i, LOW);
  }
}
```

#### Code walkthrough â€” the `for` loop

| Line | What it does | Why it matters |
| :--- | :--- | :--- |
| `for (int i = 7; i <= 9; i = i + 1)` | Start i at 7. Keep going while i â‰¤ 9. Add 1 each time. | The loop runs 3 times: i = 7, then 8, then 9 |
| `digitalWrite(i, HIGH);` | Turn ON the pin number stored in i | First time: Pin 7. Second: Pin 8. Third: Pin 9. |
| `delay(150);` | Keep it lit for 150ms | Creates the visible "chase" effect |
| `digitalWrite(i, LOW);` | Turn OFF that pin | Before moving to the next |

**The key insight:** The variable `i` becomes the pin number. One `digitalWrite(i, HIGH)` line controls three different pins. Without the loop, you'd need three separate `digitalWrite` lines.

#### 2c â€” Send to board and verify

> **EXPECTED RESULT:** LEDs light one at a time, chasing green â†’ yellow â†’ red â†’ yellow â†’ green, repeating smoothly.

| Test | Expected Result |
| :--- | :--- |
| Upload code | Compiles and uploads without errors |
| Watch LEDs | Green â†’ Yellow â†’ Red â†’ Yellow â†’ Green, repeating smoothly |
| Pattern is continuous | No long pauses between forward and backward |

---

### Step 3 â€” Challenge Extensions (If you finish early)

#### Challenge 1: Speed control

Change the `delay(150)` values. What's the fastest that still looks like a chase? What's the slowest that's still interesting?

- Fastest delay that works: _____ ms
- Slowest delay that's interesting: _____ ms

#### Challenge 2: Brightness trail

Light all three LEDs first (one `for` loop), then turn them off one by one (another `for` loop). It should look like the lights "fill up" then "drain down."

- [ ] Completed
- Observer notes: How many `for` loops did you need? _____

#### Challenge 3: Repeat exactly 3 times, then stop

Wrap the entire chase (forward + backward) in another `for` loop that runs exactly 3 times. After 3 cycles, all LEDs should stay OFF.

- [ ] Completed
- Observer notes: What did you put in the outer loop's condition? _____

---

## Troubleshooting

| Symptom | Most Likely Cause | Fix |
| :--- | :--- | :--- |
| Only red LED lights | Pins 7 and 8 not set as OUTPUT | Add `pinMode(7, OUTPUT);` and `pinMode(8, OUTPUT);` in `setup()` |
| All three LEDs light at once (no chase) | Delay too short | Increase `delay(150)` to `delay(300)` or higher |
| Only 2 LEDs chase (missing one pin) | `i <= 9` written as `i < 9` | Change `<` to `<=` to include pin 9 |
| Chase runs forever in one direction (no reverse) | Missing second `for` loop | Add the backward chase loop after the forward loop |
| Compilation error on `for` loop | Missing semicolons inside `for ( ; ; )` | The `for` header needs exactly two semicolons: `for (int i = 7; i <= 9; i = i + 1)` |
| LEDs chase in wrong color order | LEDs wired to wrong pins | Check: Green=7, Yellow=8, Red=9 |

---

## Save Your Work

1. In Arduino App Lab, click **File â†’ Save As**
2. Name: `Station__[your number]_Control_Structures` (e.g., `Station_03_Control_Structures`)
3. Save in the `Documents/Arduino` folder on the Arduino Uno Q

---

## Day 1 Progress Tracker

| Session | Status | What You Built |
| :--- | :--- | :--- |
| 1A: Code Sneak Peek | âœ“ | Watched firmware in action |
| 1B: Hello Matrix | âœ“ | First sketch from scratch â€” blinking LED |
| 1C: LED Chase Pattern | **TODAY** | For loops â€” LED chase pattern |
| 1D: Button Input | â³ Coming | If/else â€” the board makes decisions |

---

## Team Roles for This Session

| Role | Name | Responsibilities |
| :--- | :--- | :--- |
| **Coder** | | (Rotated from Session 1B) Typed code, managed Arduino App Lab |
| **Hardware Tech** | | (Rotated from Session 1B) Wired new LEDs, verified connections |
| **Observer/Documenter** | | (Rotated from Session 1B) Read lab manual, checked steps, recorded results |

> **Remember:** Roles rotate each session. Fill in your names above. Everyone should understand everything done today.

---

## Next Up

â† [Session 1B: Hello Matrix](/lab-manuals/day-01/hello-matrix/) | [Session 1D: Button Input](/lab-manuals/day-01/button-input/) â†’