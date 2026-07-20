---
title: "Electronic Buzzer (2-Wire)"
description: "Produces beeps, tones, and alerts — the easiest way to add sound to your project."
date: 2026-07-20
categories: ["output", "audio"]
---

## What Is It?

A small module with a built-in buzzer that makes sound when powered. This is an **active buzzer**, meaning it produces a tone on its own — you just turn it on and off. No complex code needed for basic beeps.

**Voltage:** 3V – 5V  
**Sound:** Fixed-pitch beep (around 2–4 kHz)

## When to Use It

- Alarm or warning signals
- Confirmation beeps (like a button press sound)
- Proximity alerts ("beep faster as you get closer")
- Game sounds and simple melodies (on/off patterns)

## Pinout

| Pin | Connect To |
|---|---|
| `+` (longer leg / marked +) | Arduino digital pin (e.g., `D9`) |
| `−` (shorter leg / marked −) | Arduino `GND` |

## How It Works (Simple)

- **Set the pin HIGH** → buzzer beeps
- **Set the pin LOW** → buzzer is silent
- **Vary the HIGH/LOW timing** → different beep patterns

For custom pitches (musical notes), you would need a *passive* buzzer and the `tone()` function. The active buzzer in your kit only plays its built-in tone.

## Example Code

```cpp
const int buzzerPin = 9;

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Single beep
  digitalWrite(buzzerPin, HIGH);
  delay(200);
  digitalWrite(buzzerPin, LOW);
  delay(300);

  // Double beep
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
  delay(100);
  digitalWrite(buzzerPin, HIGH);
  delay(100);
  digitalWrite(buzzerPin, LOW);
  delay(800);
}
```

## Common Pitfalls

- **Constant buzzing:** Make sure you set the pin LOW when you want silence. A pin left HIGH will buzz continuously.
- **Active vs passive:** This is an *active* buzzer. The `tone()` function will NOT change its pitch — it only beeps at its built-in frequency. For musical notes, you need a *passive* buzzer.
- **Reversed polarity:** The buzzer still works if backwards, but the "+" pin should go to the signal pin for correct operation.