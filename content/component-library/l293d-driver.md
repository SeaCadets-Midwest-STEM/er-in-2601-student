---
title: "L293D Motor Driver"
description: "A bridge chip that lets Arduino control motor speed and direction safely."
date: 2026-07-20
categories: ["driver", "motor"]
---

## What Is It?

The L293D is a chip that sits between your Arduino and your motor. The Arduino sends low-power signals to the L293D, and the L293D delivers the higher power the motor needs. It can control **2 DC motors** (speed + direction each) or **1 stepper motor**.

Think of it as a translator: Arduino speaks in tiny signals, the L293D shouts to the motor.

## When to Use It

- Controlling a DC motor's speed and direction
- Running two motors (like a robot with left and right wheels)
- Reversing motor direction on command
- Any time a motor needs more current than Arduino can provide

## Pinout (DIP-16 package)

| Pin | Name | Connect To |
|---|---|---|
| 1 | `1,2 EN` | Arduino PWM pin (e.g., `D10`) — Motor 1 speed |
| 2 | `1A` | Arduino digital pin (e.g., `D8`) — Motor 1 direction |
| 3 | `1Y` | Motor 1 terminal A |
| 4 | `2Y` | Motor 1 terminal B |
| 5 | `GND` | Arduino `GND` |
| 6 | `2A` | Arduino digital pin (e.g., `D9`) — Motor 1 direction |
| 7 | `VSS` | Motor power supply `5V`–`12V` (separate from Arduino) |
| 8 | `3,4 EN` | Arduino PWM pin — Motor 2 speed |
| 9 | `3A` | Arduino digital pin — Motor 2 direction |
| 10 | `4A` | Arduino digital pin — Motor 2 direction |
| 11 | `3Y` | Motor 2 terminal A |
| 12 | `4Y` | Motor 2 terminal B |
| 13 | `5,7 EN` | Arduino PWM pin — Motor 3 speed |
| 14 | `VCC` | Arduino `5V` (logic power) |
| 15 | `8,9 EN` | Arduino PWM pin — Motor 4 speed |
| 16 | `0V` | Arduino `GND` |

## Simplified Wiring (Single DC Motor)

| Connection | Where |
|---|---|
| Arduino `D8` | L293D pin 2 (`1A`) |
| Arduino `D9` | L293D pin 7 (`2A`) |
| Arduino `D10` | L293D pin 1 (`1,2 EN`) — speed control |
| Arduino `5V` | L293D pin 14 (`VCC`) |
| Arduino `GND` | L293D pin 5 and pin 12 (`GND`) |
| Motor power `5V` | L293D pin 8 (`VSS`) |
| Motor wire A | L293D pin 3 (`1Y`) |
| Motor wire B | L293D pin 4 (`2Y`) |

## Example Code

```cpp
const int dir1Pin = 8;     // direction control
const int dir2Pin = 9;     // direction control
const int speedPin = 10;   // PWM speed control

void setup() {
  pinMode(dir1Pin, OUTPUT);
  pinMode(dir2Pin, OUTPUT);
  pinMode(speedPin, OUTPUT);
}

void loop() {
  // Forward at full speed
  digitalWrite(dir1Pin, HIGH);
  digitalWrite(dir2Pin, LOW);
  analogWrite(speedPin, 255);   // 0 = stopped, 255 = full speed
  delay(2000);

  // Stop
  analogWrite(speedPin, 0);
  delay(1000);

  // Reverse at half speed
  digitalWrite(dir1Pin, LOW);
  digitalWrite(dir2Pin, HIGH);
  analogWrite(speedPin, 128);   // half speed
  delay(2000);

  // Stop
  analogWrite(speedPin, 0);
  delay(1000);
}
```

## Common Pitfalls

- **VSS vs VCC:** Pin 14 (`VCC`) is the logic voltage (5V from Arduino). Pin 8 (`VSS`) is the motor power supply. They are NOT the same.
- **Enable pin:** If the motor doesn't spin, check that the `EN` pin is set HIGH or receiving a PWM signal.
- **Heat:** The L293D gets warm under load. This is normal, but if it's too hot to touch, your motor is drawing too much current.
- **Shared ground:** The motor power supply and Arduino MUST share a common GND.