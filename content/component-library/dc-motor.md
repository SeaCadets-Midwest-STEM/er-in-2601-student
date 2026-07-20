---
title: "Micro Mini DC Motor"
description: "A tiny motor that spins when powered — great for fans, wheels, and mixing."
date: 2026-07-20
categories: ["actuator", "motor"]
---

## What Is It?

A small motor that spins in one direction when you give it power. Remove the power and it gradually stops. Think of a hair dryer fan, but tiny.

**Voltage:** 1.5V – 6V (works well at 3V or 5V from Arduino)  
**Speed:** Varies with voltage — more voltage = faster spin

## When to Use It

- Spinning a fan blade or propeller
- Driving a wheel (when paired with a motor driver)
- Mixing, stirring, or vibrating
- Any project that needs continuous rotation

## Important: Do NOT Connect Directly to Arduino

An Arduino pin can only supply a tiny amount of current. A DC motor needs more power than that, so you must use a **motor driver** (like the L293D) between the Arduino and the motor.

## Pinout

The motor has 2 wires:

| Wire | Connect To |
|---|---|
| Red (+) | Motor driver output (not directly to Arduino!) |
| Black (−) | Motor driver output |

## How to Control It

- **On/Off only:** Connect the motor through a transistor or motor driver to a digital pin
- **Speed + Direction:** Use the L293D motor driver with PWM pins

## Example Code (with L293D Driver)

See the [L293D Motor Driver](../l293d-driver/) page for a complete wiring diagram and code that controls speed and direction.

## Common Pitfalls

- **Back EMF:** A spinning motor generates voltage. When you stop it suddenly, that voltage can spike backward. The L293D driver protects against this.
- **Speed is not precise:** A DC motor spins as fast as it can. You cannot tell it to spin "exactly 90 degrees" — for that, use a servo.
- **Current draw:** A stalled motor (blocked from spinning) draws the most current. Don't leave a blocked motor powered for long.