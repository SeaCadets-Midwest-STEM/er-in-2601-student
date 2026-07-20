---
title: "KY-023 Joystick Module"
description: "A small joystick that reports X and Y position plus a push-button — like a game controller."
date: 2026-07-20
categories: ["input", "control", "analog"]
---

## What Is It?

The KY-023 is a mini joystick module with a small stick you can push in any direction. It reports the X and Y position as analog values and also acts as a button when you push the stick straight down.

Think of it as a tiny game controller: move the stick to control direction, press it to confirm.

## When to Use It

- Robot steering or tank controls
- Game controller input
- Menu navigation (up/down/left/right + select)
- Camera pan/tilte control
- Any project needing 2-direction input from one component

## Pinout

The module has 5 pins:

| Pin | Connect To | Type |
|---|---|---|
| `GND` | Arduino `GND` | Ground |
| `+5V` | Arduino `5V` | Power |
| `VRx` | Arduino `A0` | X-axis position (analog) |
| `VRy` | Arduino `A1` | Y-axis position (analog) |
| `SW` | Arduino `D2` | Push-button (digital) |

## How It Works (Simple)

The joystick contains two potentiometers — one for the X axis, one for the Y axis. Pushing the stick changes the resistance, which changes the voltage the Arduino reads.

- **Centered:** X ≈ 512, Y ≈ 512 (middle of 0–1023 range)
- **Pushed right:** X → 1023
- **Pushed left:** X → 0
- **Pushed up:** Y → 1023
- **Pushed down:** Y → 0
- **Pressed down:** SW pin goes LOW

## Example Code

```cpp
const int joyX    = A0;
const int joyY    = A1;
const int joyBtn  = 2;

void setup() {
  pinMode(joyBtn, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int xVal = analogRead(joyX);
  int yVal = analogRead(joyY);
  int btn  = digitalRead(joyBtn);

  Serial.print("X: "); Serial.print(xVal);
  Serial.print("  Y: "); Serial.print(yVal);
  Serial.print("  Button: "); Serial.println(btn);

  if (btn == LOW) {
    Serial.println(">>> Joystick pressed! <<<");
    delay(200);
  }

  delay(100);
}
```

### Using the Joystick for Robot Control (Concept)

```cpp
void loop() {
  int x = analogRead(joyX);
  int y = analogRead(joyY);

  if (x > 700) {
    // Move right
  } else if (x < 300) {
    // Move left
  } else if (y > 700) {
    // Move forward
  } else if (y < 300) {
    // Move backward
  } else {
    // Stay still (centered)
  }

  delay(50);
}
```

## Common Pitfalls

- **Not perfectly centered:** The "center" reading may not be exactly 512. Check the resting values and adjust your thresholds (e.g., treat 450–550 as "centered").
- **Jittery readings:** The values may jump around slightly. Add a small dead zone around center to avoid unwanted movement.
- **Button is active-LOW:** With `INPUT_PULLUP`, the button reads `LOW` when pressed and `HIGH` when released.
- **VRx and VRy are analog:** These pins must connect to `A` pins, not `D` pins.