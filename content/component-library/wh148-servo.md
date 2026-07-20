---
title: "WH148 Servo Motor"
description: "A small servo that moves to a specific angle you command — great for gates, arms, and steering."
date: 2026-07-20
categories: ["actuator", "servo", "motor"]
---

## What Is It?

A servo motor is a motor with built-in gears and a controller that lets you tell it to move to a specific angle (0° to 180°). Unlike a DC motor that just spins, a servo goes exactly where you point it and stays there.

**Range:** 0° to 180°  
**Voltage:** 4.8V – 6V  
**Torque:** Moderate (plastic gears)

## When to Use It

- Opening/closing a gate or flap
- Pointing a sensor or camera
- Robot arm joints
- Steering mechanism for a robot
- Any project that needs precise positioning (not just spinning)

## Pinout

The servo has a 3-wire connector:

| Wire Color | Connect To |
|---|---|
| Red (Power) | Arduino `5V` |
| Black/Brown (Ground) | Arduino `GND` |
| Orange/Yellow (Signal) | Arduino PWM pin (e.g., `D3`, marked with `~`) |

## How It Works (Simple)

You send a pulse to the signal wire. The width of the pulse tells the servo what angle to move to:

- **0.5 ms pulse** → 0° (fully counter-clockwise)
- **1.5 ms pulse** → 90° (center)
- **2.5 ms pulse** → 180° (fully clockwise)

The Arduino `Servo` library handles all of this for you — you just say `servo.write(90)` and it works.

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
  myServo.write(0);    // move to 0 degrees
  delay(1000);

  myServo.write(90);   // move to 90 degrees
  delay(1000);

  myServo.write(180);  // move to 180 degrees
  delay(1000);
}
```

## Common Pitfalls

- **Power:** Each servo can draw 100–200 mA. If you use more than one servo, you may need an external power source. Don't power multiple servos from the Arduino's 5V pin.
- **Jitter on startup:** Servos may "twitch" when the Arduino resets. This is normal.
- **PWM pin only:** The signal wire must connect to a PWM-capable pin (marked with `~` on most Arduino boards).
- **Don't force it:** Never physically force the servo horn past its limits. It can strip the internal gears.