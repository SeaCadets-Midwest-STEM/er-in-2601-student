---
title: "Micro Button Switch (NO — Normally Open)"
description: "A tiny push-button that completes a circuit when pressed — the simplest form of user input."
date: 2026-07-20
categories: ["input", "switch"]
---

## What Is It?

A small push-button with 4 legs. When you press it, an internal switch closes and electricity can flow through it. "Normally Open" (NO) means the circuit is broken until you push the button.

## When to Use It

- Starting or stopping a program
- Triggering an action on demand (sound an alarm, flash an LED)
- Resetting a counter
- Any "press to do something" interaction

## Pinout

The button has 4 pins, but they're internally paired:

```
  Pin 1 ───┐    ┌── Pin 2
           ├────┤     ← press the button to connect
  Pin 3 ───┘    └── Pin 4
```

- Pins 1 and 2 are connected to each other internally (always)
- Pins 3 and 4 are connected to each other internally (always)
- **When pressed:** all 4 pins become connected

**In practice:** You only need to use 2 pins. Connect one side to `5V` and the other side to an Arduino pin.

## Wiring

| Connection | Where |
|---|---|
| Button pin 1 | Arduino `5V` |
| Button pin 3 | Arduino digital pin (e.g., `D2`) |
| Also needed: 10kΩ resistor | From `D2` to `GND` (pull-down resistor) |

The resistor prevents the pin from "floating" (randomly reading HIGH or LOW) when the button is not pressed.

**Alternative (simpler):** Skip the external resistor and use Arduino's built-in pull-up resistor. Wire the button between `GND` and the pin, then use `INPUT_PULLUP` in code.

## Example Code (using internal pull-up — no resistor needed)

```cpp
const int buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);  // built-in resistor pulls pin HIGH
  Serial.begin(9600);
}

void loop() {
  // When button is pressed, pin reads LOW (connected to GND)
  if (digitalRead(buttonPin) == LOW) {
    Serial.println("Button pressed!");
    delay(200);  // small delay to avoid reading the same press multiple times
  }
}
```

## Common Pitfalls

- **Floating pin (without INPUT_PULLUP):** If you use `INPUT` mode without a resistor, the pin reads random values. Always use `INPUT_PULLUP` or add an external pull-down resistor.
- **Bounce:** Mechanical buttons "bounce" — the contact opens and closes rapidly when pressed. Add a short `delay(200)` after detecting a press to avoid counting one press as many.
- **Wiring all 4 pins:** You only need 2 connections. The other 2 pins are optional.