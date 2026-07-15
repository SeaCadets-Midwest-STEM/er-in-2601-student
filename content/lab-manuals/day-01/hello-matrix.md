---
title: "Lab: Hello Matrix - Your First Program"
description: "Wire an LED and write your first Arduino sketch from scratch."
date: 2025-01-01
publish_date: "2026-07-26"
session: "1B"
---

> **Session:** Session 1B - Hello Matrix: First Real Lab
> **Audience:** All teams (student-facing)
> **Time Allotted:** 90 minutes
> **Team Size:** 3 students per station
> **Prerequisites:** Session 1A (Code Sneak Peek) completed
>
> This is your first real lab. You will wire an LED to your Arduino Uno Q and write a complete program from scratch to make it blink. Then you'll experiment with different patterns.

---

## SAFETY

> **SAFETY:** Read before beginning.

1. **LED polarity matters.** The LED has two legs: a long leg (positive, called **anode**) and a short leg (negative, called **cathode**). The long leg connects to the positive side. Reversed LED = no light.
2. **Always use a resistor.** The 220 ohm resistor protects the LED from burning out. Never connect an LED directly to power without a resistor.
3. **Double-check wiring before sending code to the board.** Wrong connections won't destroy the board, but they will confuse you. Verify your connections before running your sketch.
4. **Gentle with jumper wires.** Don't bend wires at sharp angles near the plastic ends. They will crack and stop conducting.

---

## Objective

Connect an LED to your Arduino Uno Q and write a complete program that makes it blink. Then experiment with at least two different blink patterns.

---

## Parts List

Verify all items are present at your station. Check each box.

| Part | Qty | Found? |
| :--- | :--- | :--- |
| Arduino Uno Q (mounted at station) | 1 | [ ] |
| Breadboard (830-point, mounted at station) | 1 | [ ] |
| Red LED (5mm) | 1 | [ ] |
| 220 ohm resistor (color bands: red-red-brown-gold) | 1 | [ ] |
| Jumper wires (female-female, assorted colors) | 4 | [ ] |
| USB-C cable (board connected to power) | 1 | [ ] |

---

## Procedure

### Step 1 - Wire the LED Circuit (15 min)

**Hardware Tech leads. Observer reads steps. Coder watches for next step.**

The LED needs three connections: **power** (from Pin 9), **current limiting** (through the resistor), and **ground**.

#### 1a - Place the resistor

- Take the 220 ohm resistor. One end into the breadboard at any convenient row (e.g., row **C5**). The other end will stick out the other side - that's row **E5** on a standard breadboard.
- The resistor can go in any orientation - it works the same both ways.

#### 1b - Place the LED

- **Long leg (anode):** Insert into the breadboard so it connects to the resistor end (same row as **C5**). This connects the LED to the resistor.
- **Short leg (cathode):** Insert into a different row (e.g., row **C7**). This will connect to GND.

> **TIP:** If the LED is standing too tall, that's fine. Breadboards hold components loosely - don't push hard.

#### 1c - Connect Pin 9

- Take a jumper wire (any color). One end into Arduino **Pin 9** (digital pin header). Other end into the breadboard row matching the resistor side (row **E5** - same electrical row as C5).
- This carries the signal from the board to the resistor, then to the LED.

#### 1d - Connect GND

- Take another jumper wire. One end into Arduino **GND** (any GND pin). Other end into the breadboard row matching the LED short leg (row **C7** or the connected row on the other side).
- This completes the circuit: Pin 9 -> resistor -> LED -> GND.

#### 1e - Verify wiring

> **EXPECTED RESULT:** Your circuit should follow this path:
>
> **Pin 9 -> jumper wire -> 220 ohm resistor -> LED long leg (anode) -> LED short leg (cathode) -> jumper wire -> GND**
>
> Current flows from Pin 9, through the resistor (which limits current to protect the LED), through the LED (which lights up), and back to GND. The LED lights when Pin 9 is set to HIGH (5V).

- [ ] Resistor is in series with the LED (between Pin 9 and the LED, or between the LED and GND - both work)
- [ ] LED long leg is on the Pin 9 side
- [ ] LED short leg connects to GND
- [ ] No loose wires

**Call an instructor to verify your wiring before proceeding.**

---

### Step 2 - Write Your First Sketch (30 min)

**Coder types. Observer reads instructions aloud. Hardware Tech watches for mistakes.**

#### 2a - Open Arduino App Lab

- On your Arduino Uno Q's connected monitor, open **Arduino App Lab** to launch the IDE.
- Because Arduino App Lab runs directly on the board, the correct board is already selected - no board or port configuration needed.

#### 2b - Create a new sketch

- Tap the **New Sketch** button (plus/+ icon) on the toolbar to open a blank editor.
- Do NOT open the Blink example. You're writing this from scratch.

#### 2c - Type the header comment

Every program you write this week starts with a header comment. Type this block, filling in your team info:

```cpp
/*
 * Session 1B: Hello Matrix
 * Team ___ - Creation Station #___
 * Purpose: Blink an external LED on Pin 9
 * Expected result: LED turns on for 1 second, off for 1 second, repeating
 */
```

> **INSTRUCTOR NOTE:** Comments that start with `/*` and end with `*/` are ignored by the microcontroller. They're for humans - notes that explain what the code does.

#### 2d - Type the `setup()` function

Below the header comment, type:

```cpp
void setup() {
  pinMode(9, OUTPUT);
}
```

**What this does:**

- `void setup() {` - "This block runs ONCE when the board powers on."
- `pinMode(9, OUTPUT);` - "Prepare Pin 9 to SEND power (OUTPUT mode) to something connected to it."
- `}` - "End of setup."

#### 2e - Type the `loop()` function

Below the `setup()` function (leave a blank line), type:

```cpp
void loop() {
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);
  delay(1000);
}
```

**What this does:**

- `void loop() {` - "This block repeats FOREVER."
- `digitalWrite(9, HIGH);` - "Send 5 volts OUT of Pin 9. The LED turns ON."
- `delay(1000);` - "Wait 1000 milliseconds (1 second)."
- `digitalWrite(9, LOW);` - "Set Pin 9 to 0 volts. The LED turns OFF."
- `delay(1000);` - "Wait 1 second again."
- `}` - "End of loop. Go back to the top and repeat."

#### 2f - Check your complete sketch

Your full sketch should look exactly like this:

```cpp
/*
 * Session 1B: Hello Matrix
 * Team ___ - Creation Station #___
 * Purpose: Blink an external LED on Pin 9
 * Expected result: LED turns on for 1 second, off for 1 second, repeating
 */

void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);
  delay(1000);
}
```

**Self-check before running:**

- [ ] Header comment is filled in with team info
- [ ] Every line ends with a semicolon `;` (except the `void` lines and curly braces)
- [ ] Opening `{` has a matching closing `}`
- [ ] Pin number is `9` everywhere (not `13`)

---

### Step 3 - Send Code to Board and Verify (10 min)

#### 3a - Send to board

- Tap the **Verify** button (checkmark icon) on the toolbar first. This compiles your code and checks for errors.
- If you see errors in red text at the bottom of the screen, fix the first error and try again. Common errors are listed in Troubleshooting below.
- When verification passes, click the **Upload** button (right-arrow icon) on the toolbar to transfer your sketch to the Arduino board.

#### 3b - Observe

> **EXPECTED RESULT:** The red LED blinks ON for 1 second, then OFF for 1 second, repeating at a steady rhythm.

- [ ] LED blinks at steady 1-second rhythm
- [ ] Pattern repeats without stopping

**If the LED does not blink, check Troubleshooting below before calling an instructor.**

---

### Step 4 - Pattern Challenge (25 min)

**Now experiment. Change the `delay()` values to create different patterns. Send the updated sketch to the board after each change.**

Complete at least **TWO** patterns from this list. Record your results.

#### Pattern 1: Morse Code SOS

Short-short-short, long-long-long, short-short-short.

```cpp
void loop() {
  // S: three short blinks
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(500);

  // O: three long blinks
  digitalWrite(9, HIGH); delay(500); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(500); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(500); digitalWrite(9, LOW); delay(500);

  // S: three short blinks
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(200);
  digitalWrite(9, HIGH); delay(200); digitalWrite(9, LOW); delay(1000);
}
```

- [ ] Completed - LED flashes SOS pattern
- Observer notes: What do the short and long blinks feel like?

#### Pattern 2: Heartbeat

Thump-thump... pause... thump-thump.

```cpp
void loop() {
  digitalWrite(9, HIGH); delay(150); digitalWrite(9, LOW); delay(300);
  digitalWrite(9, HIGH); delay(150); digitalWrite(9, LOW); delay(1000);
}
```

- [ ] Completed - LED pulses like a heartbeat
- Observer notes: How many "beats" per minute does this feel like?

#### Pattern 3: Police Light

Very fast, equal on and off.

- [ ] Completed
- Record in your notebook: Your delay values for ON and OFF

#### Pattern 4: Lighthouse

Quick flash, long pause.

- [ ] Completed
- Record in your notebook: Your delay values for ON and OFF

#### Pattern 5: Custom

Invent your own pattern. Write the description and the code.

- [ ] Completed
- Record in your notebook: Pattern name and a description of what it looks like

---

## Troubleshooting

| Symptom | Most Likely Cause | Fix |
| :--- | :--- | :--- |
| LED doesn't light at all | LED reversed | Swap the LED legs. Long leg -> Pin 9 side. Short leg -> GND side. |
| LED doesn't light at all | Missing resistor | Add the 220 ohm resistor in series with the LED. |
| LED stays ON, doesn't blink | Sketch not sent to board | Click Upload again. Check status bar says "Done transferring." |
| LED stays ON, doesn't blink | Both delay values = 0 | Change delays to at least 100. |
| Compilation error in red text | Missing semicolon | Look at the line BEFORE the error. Add `;` at end of statement. |
| "pinMode was not declared" | Compilation error (not board-related) | Check spelling of `pinMode`. First letter lowercase P, rest lowercase. Common typo: `PinMode` or `PINMODE`. |
| Sketch does not transfer to board | Connection issue | Make sure the USB-C power cable is seated. Click the Upload button again. If it persists, call an instructor. |
| LED is very dim | LED reversed (leaking current) | Swap LED legs. An LED backward will glow faintly. |

---

## Save Your Work

1. Tap the **Save** icon (disk icon) on the toolbar.
2. Name the sketch: `Station__[number]_Hello_Matrix` (e.g., `Station_03_Hello_Matrix`)
3. Confirm the sketch saves to the Arduino Uno Q's local storage.
4. Observer/Documenter: Record in this manual which patterns your team completed and any notes.

---

## Challenge Extensions (If You Finish Early)

- **Three LEDs:** Can you wire a second LED on a different pin and make them blink in alternating patterns?
- **Faster each cycle:** Can you make the blink speed increase? (Try changing delay values to smaller numbers each loop - this is harder than it sounds!)
- **Explain it:** Can your team explain every line of code to another team? Teaching is the best test of understanding.

---

## Team Roles for This Session

| Role | Name | Responsibilities |
| :--- | :--- | :--- |
| **Coder** | | Typed code, managed Arduino App Lab, sent sketches to board |
| **Hardware Tech** | | Wired the circuit, verified connections, managed parts |
| **Observer/Documenter** | | Read lab manual aloud, checked off steps, recorded pattern results |

> **Remember:** Roles rotate next session. Everyone should understand everything done today.

---

## Next Up

Continue to [Session 1C: LED Chase Pattern](/lab-manuals/day-01/led-chase/) ->