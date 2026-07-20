---
title: "LED Assortment (Red, Green, Yellow, Blue, Orange, Clear)"
description: "Tiny lights that turn on when current flows through them — the simplest visual output."
date: 2026-07-20
categories: ["output", "led", "indicator"]
---

## What Is It?

An LED (Light Emitting Diode) is a component that glows when electricity flows through it in the correct direction. Your assortment includes multiple colors: red, green, yellow, blue, orange, and clear (white light).

**Forward voltage:** ~1.8V (red/yellow) to ~3.3V (blue/white)  
**Current:** 20 mA maximum (use a resistor to limit current!)

## When to Use It

- Visual indicators (on/off, status, alerts)
- Color-coded signals (red = stop, green = go)
- Simple bar graphs or patterns
- Decorative lighting
- Debugging (flash an LED to confirm code is running)

## Pinout

An LED has 2 legs:

| Leg | Connect To |
|---|---|
| **Anode** (longer leg) | Arduino digital pin **through a resistor** (e.g., 220Ω or 330Ω) |
| **Cathode** (shorter leg, flat edge on the plastic) | Arduino `GND` |

> **CRITICAL:** Always use a resistor in series with the LED. Connecting an LED directly to 5V will burn it out or damage the Arduino pin. A **220Ω resistor** is a safe choice for all colors.

## How It Works (Simple)

- **Set the pin HIGH** → current flows → LED lights up
- **Set the pin LOW** → no current → LED is off
- **Use `analogWrite()` on a PWM pin** → vary brightness (0 = off, 255 = full)

## Example Code

```cpp
const int ledPin = 9;  // use a PWM pin (~9) for brightness control

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn on full brightness
  digitalWrite(ledPin, HIGH);
  delay(500);

  // Fade out using PWM
  for (int brightness = 255; brightness > 0; brightness -= 10) {
    analogWrite(ledPin, brightness);
    delay(30);
  }

  // Off
  analogWrite(ledPin, 0);
  delay(500);
}
```

## Wiring Diagram

```
5V (or digital pin) ── [220Ω Resistor] ── LED (long leg → short leg) ── GND
```

## Common Pitfalls

- **No resistor = burned LED:** This is the #1 mistake. Always include a current-limiting resistor. 220Ω is safe for all colors.
- **Backwards:** LEDs only work in one direction. If it doesn't light up, try flipping the LED. The longer leg goes toward the positive side.
- **Wrong color brightness:** Blue and white LEDs need more voltage than red. They may look dimmer with the same resistor. Try a smaller resistor (150Ω) for blue/white if needed.
- **PWM for brightness:** Only pins marked with `~` support `analogWrite()` for dimming.