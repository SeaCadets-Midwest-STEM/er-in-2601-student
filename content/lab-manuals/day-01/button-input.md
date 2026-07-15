---
title: "Lab: Button Input â€” If/Else Decision Making"
description: "Wire a pushbutton and write code that makes the board change behavior based on input."
date: 2026-07-26
publishDate: 2026-07-26
session: "1D"
---

> **Session:** Day 1, Session 1D (Afternoon Block 2)
> **Duration:** 25 minutes (hands-on portion)
> **Prerequisites:** Session 1C completed â€” LEDs on Pins 7, 8, 9 already wired
>
> **SAFETY:** 5V logic. No high voltage. No heat. Standard electronics safety: do not short 5V to GND with a wire while the board is powered.

---

## Objective

Give your Arduino its first sense. Wire a pushbutton and write code that makes the board change behavior based on whether the button is pressed.

---

## Parts List (Per Station)

| Part | Qty | Notes |
| :--- | :--- | :--- |
| Arduino Uno Q (mounted) | 1 | Already at station |
| Breadboard | 1 | Three LEDs already wired from Lab 1C |
| Red/Yellow/Green LEDs + resistors | 3 | Pins 9, 8, 7 â€” from Lab 1C |
| **Pushbutton (6-leg)** | **1** | **NEW â€” wire to Pin 2** |
| **10kÎ© resistor** | **1** | **NEW â€” pull-down resistor** |
| Jumper wires (female-female) | 2+ | Additional for button circuit |

---

## Part 1: Wire the Pushbutton (5 minutes)

### The button circuit

A pushbutton needs a **pull-down resistor** to give the pin a known state when the button is NOT pressed. Without it, the pin "floats" and reads random values.

### Wiring

- **5V** â†’ one side of the button (jumper wire)
- **Other side of button** â†’ **Pin 2** (jumper wire)
- **Other side of button** â†’ **10kÎ© resistor** â†’ **GND** (this is the pull-down)
- 6-leg buttons: the two legs on the same side are internally connected. Wire to opposite sides.

### Steps

1. **Place the pushbutton** on the breadboard, straddling the center groove.
2. **Connect 5V** to one side of the button with a jumper wire.
3. **Connect Pin 2** to the other side of the button with a jumper wire.
4. **Connect the 10kÎ© resistor** from the Pin 2 side to **GND**.
5. **Verify:** One side of button gets 5V. Other side goes to Pin 2 AND to GND through the 10kÎ© resistor.

> **How it works:** When the button is NOT pressed, the 10kÎ© resistor pulls Pin 2 to GND = reads LOW (0). When pressed, 5V connects directly to Pin 2 = reads HIGH (1). The resistor prevents a short circuit from 5V to GND when the button is pressed.

### Self-check

- [ ] Button straddles the center groove
- [ ] One side connected to 5V
- [ ] Other side connected to Pin 2
- [ ] 10kÎ© resistor from Pin 2 side to GND (pull-down)

**Call an instructor to verify wiring before proceeding.**

---

## Part 2: Read the Button (15 minutes)

### Type this code into your editor

```cpp
/*
 * Session 1D: Button Input
 * Team ___ â€” Creation Station #___
 * Purpose: Turn on LED when button is pressed
 * Expected result: Red LED (Pin 9) lights when button pressed, off when released
 */

const int buttonPin = 2;
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

### Code walkthrough â€” `if/else`

| Line | What it does | Why it matters |
| :--- | :--- | :--- |
| `const int buttonPin = 2;` | Name Pin 2 as "buttonPin" | Makes code readable. `const` = value never changes. |
| `int buttonState = digitalRead(buttonPin);` | Read the button and save the result | `digitalRead` returns HIGH (1) or LOW (0) |
| `if (buttonState == HIGH)` | "If the button is pressed..." | `==` compares two values. Single `=` would be an assignment error! |
| `{ digitalWrite(ledPin, HIGH); }` | ...turn the LED on | Inside the `if` block = only runs when condition is true |
| `else { digitalWrite(ledPin, LOW); }` | ...otherwise turn it off | The `else` block runs when the `if` condition is false |

**The key insight:** `if/else` is a decision. The board reads input, makes a choice, and acts differently based on that choice. This is the foundation of all interactive programs.

### Verify

| Test | Expected Result |
| :--- | :--- |
| Button NOT pressed | Red LED (Pin 9) is OFF |
| Button pressed | Red LED (Pin 9) lights up |
| Button released | Red LED turns OFF |
| Press and release rapidly | LED follows button perfectly |

> **EXPECTED RESULT:** Red LED turns ON when button is pressed, OFF when released. No delay, no flickering.

---

## Challenge Extensions (If you finish early)

### Challenge 1: Toggle mode

Instead of "hold to light," make the LED toggle: press once = ON, press again = OFF, press again = ON. The LED should stay ON after you release the button.

- [ ] Completed
- Record in your notebook: What variable did you use to track the state?

### Challenge 2: Color cycler

Use the button to cycle through the three LEDs: press = green, press = yellow, press = red, press = green... Each press advances to the next color.

- [ ] Completed
- Record in your notebook: What control structure did you use?

### Challenge 3: Button-controlled chase speed

Combine the chase pattern from Session 1C with the button: button pressed = fast chase, button released = slow chase.

- [ ] Completed
- Record in your notebook: Fast delay and slow delay values in milliseconds

---

## Troubleshooting

| Symptom | Most Likely Cause | Fix |
| :--- | :--- | :--- |
| LED always ON (button does nothing) | Button wired backwards (5V on Pin 2 side, resistor on 5V side) | Swap: 5V â†’ button â†’ Pin 2. Resistor from Pin 2 â†’ GND. |
| LED flickers randomly | Missing pull-down resistor | Add 10kÎ© resistor from Pin 2 to GND |
| LED never turns on when pressed | Pin 2 not reading correctly | `digitalRead(buttonPin)` â€” make sure Pin 2 is NOT set as OUTPUT in setup() |
| `==` error in code | Used single `=` instead of `==` in if condition | Change `if (buttonState = HIGH)` to `if (buttonState == HIGH)` |
| Compilation error: "HIGH not declared" | Typo | Check: `HIGH` (all caps), not `High` or `high` |
| Button feels mushy, no click | Button not seated in breadboard | Press down firmly. All 6 legs should be in holes. |

---

## Save Your Work

1. In Arduino App Lab, click **File â†’ Save As**
2. Name: `Station__[your number]_Button_Input` (e.g., `Station_03_Button_Input`)
3. Save in the `Documents/Arduino` folder on the Arduino Uno Q

---

## Day 1 Progress Tracker

| Session | Status | What You Built |
| :--- | :--- | :--- |
| 1A: Code Sneak Peek | âœ“ | Watched firmware in action |
| 1B: Hello Matrix | âœ“ | First sketch from scratch â€” blinking LED |
| 1C: Control Structures | âœ“ | For loops â€” LED chase pattern |
| 1D: Button Input | **COMPLETED** | If/else â€” the board makes decisions |

---

## Team Roles for This Session

| Role | Name | Responsibilities |
| :--- | :--- | :--- |
| **Coder** | | (Rotated from Session 1C) Typed code, managed Arduino App Lab |
| **Hardware Tech** | | (Rotated from Session 1C) Wired button, verified connections |
| **Observer/Documenter** | | (Rotated from Session 1C) Read lab manual, checked steps, recorded results |

> **Remember:** Roles rotate each session. Record your team roles in your notebook. Everyone should understand everything done today.

---

## Day 1 Complete! ðŸŽ‰

You've written three programs from scratch, wired four components, and learned the core building blocks of firmware: **outputs**, **loops**, and **decisions**. Tomorrow you'll add sensors to give your board the ability to measure the real world.

---

## Previous / Next

â† [Session 1C: LED Chase Pattern](/lab-manuals/day-01/led-chase/) | [Day 2: Sensors and Analog Input](/lab-manuals/day-02/) â†’