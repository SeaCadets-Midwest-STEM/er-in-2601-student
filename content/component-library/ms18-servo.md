---
title: "MS18 Servo Motor"
description: "A compact, lightweight servo for precise angular positioning — ideal for small mechanisms."
date: 2026-07-20
categories: ["actuator", "servo", "motor"]
---

## What Is It?

The MS18 is a small, lightweight servo motor. Like the WH148, it moves to a specific angle (0° to 180°) and holds it. The MS18 is typically smaller and lighter, making it ideal for compact projects.

**Range:** 0° to 180°  
**Voltage:** 4.8V – 6V  
**Torque:** Light (smaller than WH148 — best for lightweight loads)

## When to Use It

- Small robot arm joints
- Camera or mirror tilting
- Flaps, doors, or gates on a model
- Fan blades or directional controls
- Any project needing precise positioning in a small package

## Pinout

The servo has a 3-wire connector:

| Wire Color | Connect To |
|---|---|
| Red (Power) | Arduino `5V` |
| Black/Brown (Ground) | Arduino `GND` |
| Orange/Yellow (Signal) | Arduino PWM pin (e.g., `D3`, marked with `~`) |

## How It Works (Simple)

Identical to the WH148: you send a pulse, and the servo moves to the matching angle. The Arduino `Servo` library handles everything:

- `servo.write(0)` → 0° (fully counter-clockwise)
- `servo.write(90)` → 90° (center)
- `servo.write(180)` → 180° (fully clockwise)

## Example Code

```cpp
#include <Servo.h>

Servo myServo;
const int servoPin = 3;

void setup() {
  myServo.attach(servoPin);
  myServo.write(90);  // start at center
}

void loop() {
  // Sweep from 0 to 180 and back
  for (int angle = 0; angle <= 180; angle += 1) {
    myServo.write(angle);
    delay(15);
  }
  for (int angle = 180; angle >= 0; angle -= 1) {
    myServo.write(angle);
    delay(15);
  }
}
```

## MS18 vs WH148 — Which Should I Use?

| Feature | MS18 | WH148 |
|---|---|---|
| **Size** | Smaller | Larger |
| **Torque** | Light | Moderate |
| **Best for** | Lightweight, compact projects | Heavier loads, more force needed |
| **Wiring** | Identical (3-wire) | Identical (3-wire) |
| **Code** | Identical (`Servo` library) | Identical (`Servo` library) |

**Rule of thumb:** Use the MS18 for light, compact projects. Use the WH148 when you need more force.

## Common Pitfalls

- **Not enough torque:** The MS18 is small. If the servo struggles or vibrates, the load is too heavy — switch to the WH148.
- **Power:** Even a small servo draws 50–100 mA. Multiple servos need an external power source.
- **Jitter on reset:** Servos twitch when Arduino restarts. This is normal.
- **Don't force the horn:** Never push the servo past its limits by hand.