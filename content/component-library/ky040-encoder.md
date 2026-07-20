---
title: "KY-040 Rotary Encoder"
description: "A knob you can turn left/right and press down — perfect for menus and volume controls."
date: 2026-07-20
categories: ["input", "control"]
---

## What Is It?

A rotary encoder is a knob that reports how much and which direction you turned it. Unlike a potentiometer (which gives a position), the encoder gives you *changes*: "turned 1 click clockwise" or "turned 2 clicks counter-clockwise." It also has a built-in push-button.

## When to Use It

- Volume or brightness controls
- Scrolling through menus
- Selecting values (speed, threshold, timer)
- Any interface where you want "more" or "less" rather than a specific position

## Pinout

| Pin | Connect To |
|---|---|
| `+` | Arduino `5V` |
| `-` | Arduino `GND` |
| `S` | Arduino `GND` |
| `CLK` (or `DT`) | Arduino digital pin `D2` (interrupt-friendly) |
| `DAT` (or `SW`) | Arduino digital pin `D3` |

> **Note:** Pin labels vary by manufacturer. The 5 pins are typically: `+`, `-`, `S`, `CLK`, `DAT`. The `S` pin is the internal switch (button) ground — connect it to `GND`.

## How It Works (Simple)

As you turn the knob, two internal contacts (called A and B) open and close in sequence. By watching which one changes first, the Arduino knows the direction:

- **A changes before B** = Clockwise
- **B changes before A** = Counter-clockwise

The push-button is a separate switch between the `+` and `CLK` pins internally. Pressing it pulls the `CLK` pin LOW.

## Example Code

```cpp
const int clkPin = 2;
const int datPin = 3;
const int swPin  = 4;   // button (optional separate pin)

int encoderCount = 0;
bool lastState = false;

void setup() {
  pinMode(clkPin, INPUT);
  pinMode(datPin, INPUT);
  pinMode(swPin, INPUT_PULLUP);

  Serial.begin(9600);
}

void loop() {
  bool currentState = digitalRead(clkPin);
  if (currentState != lastState) {
    // Direction depends on DAT pin
    if (digitalRead(datPin) != currentState) {
      encoderCount++;       // clockwise
    } else {
      encoderCount--;       // counter-clockwise
    }
    Serial.print("Position: ");
    Serial.println(encoderCount);
  }
  lastState = currentState;

  // Check button press
  if (digitalRead(swPin) == LOW) {
    Serial.println("Button pressed!");
    encoderCount = 0;       // reset on press
    delay(200);
  }

  delay(1);
}
```

## Common Pitfalls

- **Jittery readings:** The contacts "bounce" when turning, which can cause extra counts. Adding a small `delay(1)` or using interrupts helps.
- **No zero position:** Unlike a potentiometer, the encoder has no "home" position. Your code must track the starting value.
- **Pin labels differ:** Check your module. Some label the pins `CLK`/`DT`/`SW`; others use `A`/`B`/`SW`.